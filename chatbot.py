import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create client
client = OpenAI(api_key=api_key)

def get_chat_response(messages, temperature=0.7):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"