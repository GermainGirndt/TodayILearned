# Split text phrases using regex and print results to a file

import re
texto = "Compartilhe um valor seu Conte um pouco sobre a sua história Compartilhe algo sobre disciplina Comente uma polêmica que envolve sua área de atuação Anuncie uma live e comente sobre o tema Fale sobre um assunto quente envolvendo o seu nicho Indique um livro Mostre os bastidores do seu trabalho Dê uma dica de app que te ajuda diariamente Revele parte do seu processo de criação Faça um pequeno review sobre algum filme ou série que assistiu Relate como começou a criar conteúdo Fale sobre um desafio do seu negócio Peça ajuda da sua comunidade para alguma tomada de decisão Indique um perfil ou uma pessoa que te inspire Faça um TOP 5 (de música, roupas, livros, filmes, apps...) Conte algo sobre sua família ou sobre seu pet Divulgue uma novidade envolvendo seu trabalho Converse sobre alguma mudança ou transformação Revele uma vulnerabilidade sua Compartilhe um marco da sua história Relate uma história engraçada Compartilhe o retorno de clientes sobre seus produtos ou serviços Diga para os seus seguidores o que faz no tempo livre Comente sobre mentalidade ou frase de inspiração (com algo que envolva seu nicho) Responda dúvidas do seu nicho Mostre um equipamentode trabalho que te auxilia Crie um quiz envolvendo sua marca ou seu nicho Compartilhe sua rotina por um dia Reposte um meme"

frases = re.compile(r"([A-Z]([A-Z]{3,}?|[^A-Z]*)*)").split(texto)
print(frases)

with open('result.txt', 'w') as file:
    for frase in frases:
        if frase != "":
            file.write(frase)
            file.write("\n")
