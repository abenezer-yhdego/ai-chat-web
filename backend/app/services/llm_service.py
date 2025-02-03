import openai
from app.config import Config

openai.api_key = Config.OPENAI_API_KEY

def get_llm_response(message, context=""):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": context + "\n" + message}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
