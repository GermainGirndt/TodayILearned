import os
import openai
import json
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API


def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)


# define a function
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
response_choises = response.choices
print(response_choises)


print("\nFirst Choice:")
print(response_choises[0])


print("\nFirst Choice Message:")
response_choise_message = response_choises[0].message
print(response_choise_message)

print(response_choise_message.content)
print(response_choise_message.function_call)
json.loads(response_choise_message.function_call.arguments)
args = json.loads(response_choise_message.function_call.arguments)

observation = get_current_weather(args)

print("\n-------------------")
print("\nFunction Response:")
print(observation)


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
