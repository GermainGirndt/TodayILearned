import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import OpenAI from 'openai';
import { FormMessage, RequestBody, ResponseBody } from './interfaces';

type MissingInformationGuard = {
  isMissingInformation: boolean;
  suggestion: string;
};

type IncongruentInformationGuard = {
  isIncongruent: boolean;
  suggestion: string;
};

type TranslationResult = {
  translation: string;
};

@Injectable()
export class AppService {
  private readonly openai: OpenAI;
  private readonly REQUIRED_INFORMATION_VECTOR_STORE_ID: string = '';

  constructor(private readonly config: ConfigService) {
    this.openai = new OpenAI({
      apiKey: this.config.getOrThrow<string>('OPEN_AI_KEY'),
    });
  }

  public async handleWorkflowStep(
    requestBody: RequestBody,
  ): Promise<ResponseBody> {
    const { action, history } = requestBody;

    if (history.length === 0) {
      throw new Error('History cannot be empty');
    }

    const lastMessage = history[history.length - 1];

    if (action === 'CHECK_QUALITY') {
      return {
        action: 'CHECK_QUALITY',
        improvementSuggestions:
          await this.generateImprovementSuggestions(history),
      };
    }

    if (action === 'SUBMIT_FOR_NEXT_STEP') {
      let translation: string;

      if (lastMessage.role === 'Technical') {
        translation =
          await this.generateTranslationFromTechnicalToLegal(history);
      } else if (lastMessage.role === 'Legal') {
        translation =
          await this.generateTranslationFromLegalToTechnical(history);
      } else {
        throw new Error(`Unsupported message role: ${lastMessage.role}`);
      }

      return {
        action: 'SUBMIT_FOR_NEXT_STEP',
        translation,
      };
    }

    throw new Error('Unsupported action');
  }

  public async generateImprovementSuggestions(
    history: FormMessage[],
  ): Promise<string[]> {
    const improvementSuggestions: string[] = [];

    const missingInformationGuard = await this.checkMissingInformation(history);

    if (
      missingInformationGuard.isMissingInformation &&
      missingInformationGuard.suggestion.trim().length > 0
    ) {
      improvementSuggestions.push(missingInformationGuard.suggestion);
    }

    const incongruentInformationGuard =
      await this.checkIncongruentInformation(history);

    if (
      incongruentInformationGuard.isIncongruent &&
      incongruentInformationGuard.suggestion.trim().length > 0
    ) {
      improvementSuggestions.push(incongruentInformationGuard.suggestion);
    }

    return improvementSuggestions;
  }

  private async checkMissingInformation(
    history: FormMessage[],
  ): Promise<MissingInformationGuard> {
    const input = JSON.stringify({ history });
    console.log('checkMissingInformation input:', input);
    const response = await this.openai.responses.create({
      model: 'gpt-4.1-mini',
      instructions: `
You are reviewing a GDPR personal data breach notification workflow.

Check whether the form message history is missing important information.

Relevant required information (which might be missing) depending on the use case, depending on the case, are contained in the documents in the vector store.

Return exactly one concise suggestion if important information is missing.
If nothing important is missing, return isMissingInformation=false and suggestion="".
Do not invent facts.
      `.trim(),
      input,
      tools: [
        {
          type: 'file_search',
          vector_store_ids: [this.REQUIRED_INFORMATION_VECTOR_STORE_ID],
          max_num_results: 5,
        },
      ],
      text: {
        format: {
          type: 'json_schema',
          name: 'missing_information_guard',
          strict: true,
          schema: {
            type: 'object',
            additionalProperties: false,
            properties: {
              isMissingInformation: {
                type: 'boolean',
              },
              suggestion: {
                type: 'string',
              },
            },
            required: ['isMissingInformation', 'suggestion'],
          },
        },
      },
    });

    return JSON.parse(response.output_text) as MissingInformationGuard;
  }

  private async checkIncongruentInformation(
    history: FormMessage[],
  ): Promise<IncongruentInformationGuard> {
    const input = JSON.stringify({ history });
    console.log('checkIncongruentInformation input:', input);
    const response = await this.openai.responses.create({
      model: 'gpt-4.1-mini',
      instructions: `
You are reviewing a GDPR personal data breach notification workflow.

Check whether the form message history contains incongruent, contradictory, or unclear information.

Examples:
- one message says a lost laptop was encrypted, another says it was not encrypted
- one message says no personal data was affected, another lists affected data subjects
- one message says remote wipe succeeded, another says device access is unknown
- one message says no special-category data exists, another references health, biometric, political, religious, or similar data
- dates or incident timelines contradict each other

Return exactly one concise suggestion explaining what should be clarified or corrected.
If there is no incongruent information, return isIncongruent=false and suggestion="".
Do not invent contradictions.
      `.trim(),
      input,
      text: {
        format: {
          type: 'json_schema',
          name: 'incongruent_information_guard',
          strict: true,
          schema: {
            type: 'object',
            additionalProperties: false,
            properties: {
              isIncongruent: {
                type: 'boolean',
              },
              suggestion: {
                type: 'string',
              },
            },
            required: ['isIncongruent', 'suggestion'],
          },
        },
      },
    });

    return JSON.parse(response.output_text) as IncongruentInformationGuard;
  }

  public async generateTranslationFromTechnicalToLegal(
    history: FormMessage[],
  ): Promise<string> {
    const lastMessage = history[history.length - 1];

    const input = JSON.stringify({
      latestMessage: lastMessage,
      fullHistory: history,
    });
    console.log(`generateTranslationFromTechnicalToLegal input: ${input}`);

    const response = await this.openai.responses.create({
      model: 'gpt-4.1-mini',
      instructions: `
You translate technical incident information into language useful for a legal/privacy team.

Requirements:
- rewrite the expresssions, translating the technical details into simple language that a legal team can understand
- preserve all facts from the latest technical message
- use the broader history only for context
- do not invent missing facts
- keep it simple and concise, focusing on the key facts that a legal team would need to know for GDPR compliance assessment and potential notification
- mention uncertainty where the technical facts are unclear
      `.trim(),
      input,
      text: {
        format: {
          type: 'json_schema',
          name: 'technical_to_legal_translation',
          strict: true,
          schema: {
            type: 'object',
            additionalProperties: false,
            properties: {
              translation: {
                type: 'string',
              },
            },
            required: ['translation'],
          },
        },
      },
    });

    const parsed = JSON.parse(response.output_text) as TranslationResult;
    return parsed.translation;
  }

  public async generateTranslationFromLegalToTechnical(
    history: FormMessage[],
  ): Promise<string> {
    const lastMessage = history[history.length - 1];

    const input = JSON.stringify({
      latestMessage: lastMessage,
      fullHistory: history,
    });
    console.log(`generateTranslationFromLegalToTechnical input: ${input}`);

    const response = await this.openai.responses.create({
      model: 'gpt-4.1-mini',
      instructions: `
You translate legal/privacy incident information into language useful for a technical/security team.

Requirements:
- simplify legal and GDPR terminology so that a technical team can understand the key facts and requirements
- preserve all facts from the latest legal message
- use the broader history only for context
- do not invent missing facts
- focus on concrete technical explicitly suggested by the legal message, such as specific mitigation measures, timelines, or data categories that require special handling
- mention uncertainty where the legal request is unclear
- your answer should be concise and simple
      `.trim(),
      input,
      text: {
        format: {
          type: 'json_schema',
          name: 'legal_to_technical_translation',
          strict: true,
          schema: {
            type: 'object',
            additionalProperties: false,
            properties: {
              translation: {
                type: 'string',
              },
            },
            required: ['translation'],
          },
        },
      },
    });

    const parsed = JSON.parse(response.output_text) as TranslationResult;
    return parsed.translation;
  }
}
