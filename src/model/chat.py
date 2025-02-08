import os

import dotenv
import openai

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def chat_template(user_message: str) -> list[dict[str, str]]:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message},
    ]
    return messages


def chat(user_message: str) -> str:
    client = openai.OpenAI()
    messages = chat_template(user_message)
    client.api_key = OPENAI_API_KEY
    response = client.chat.completions.create(model="gpt-4o", messages=messages)
    return response.choices[0].message.content
