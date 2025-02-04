import os
import openai

def chat_template(user_message: str) -> list[dict[str, str]]:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }, 
        {
            "role": "user",
            "content": user_message
        }
    ]
    return messages