import os
import openai
import json
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API


def get_current_weather(location):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location["location"],
        "temperature": "27",
        "unit": location["unit"],
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)


# define a function
# be aware that the function name should match the name of the function in the code
# and that the token limit also apply to the function
functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
]

system_message = {
    "role": "system",
    "content": f"You're an weather expert. Answer the user query in an polite and comprehensive way. Use always metric units."
}

user_message = {
    "role": "user",
    "content": "What's the weather like in Boston?"
}

messages = [
    system_message,
    user_message
]

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions
)

print("\nResponse:")
print(response)

print("\nChoices:")
response_choices = response.choices
print(response_choices)


first_choice = response_choices[0]

print("\nFirst Choice:")
print(first_choice)


print("\nFirst Choice Message:")
response_choice_message = first_choice.message
print(response_choice_message)

print("\nFunction Call:")
print(response_choice_message.function_call)

if response_choice_message.function_call and response_choice_message.function_call.name == "get_current_weather":
    print("\n-------------------")
    print("\n Function Call 'get_current_weather' detected.")
    print("\n Executing...")
    json.loads(response_choice_message.function_call.arguments)
    args = json.loads(response_choice_message.function_call.arguments)

    observation = get_current_weather(args)

    print("\nFunction Response (Observation):")
    print(observation)
    print("\n-------------------")
    
    
    print("\nInserting observation into messages...")


    observation_message = {
        "role": "function",
                "name": "get_current_weather",
                "content": observation,
    }

    messages.append(observation_message)

    print(messages)

    informed_response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions
    )

    print("\nInformed Response:")
    print(informed_response)


# Alternative:


"""

from langchain.utils.openai_functions import convert_pydantic_to_openai_function

class WeatherSearch(BaseModel):
    `Call this with an airport code to get the weather at that airport`
    airport_code: str = Field(description="airport code to get weather for")
    
weather_function = convert_pydantic_to_openai_function(WeatherSearch)
weather_function
"""
# Result:
""" {'name': 'WeatherSearch',
 'description': 'Call this with an airport code to get the weather at that airport',
 'parameters': {'title': 'WeatherSearch',
  'description': 'Call this with an airport code to get the weather at that airport',
  'type': 'object',
  'properties': {'airport_code': {'title': 'Airport Code',
    'description': 'airport code to get weather for',
    'type': 'string'}},
  'required': ['airport_code']}} """
