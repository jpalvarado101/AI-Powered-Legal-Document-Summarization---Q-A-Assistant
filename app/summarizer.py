import openai
import os

# Get the API key from the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

def summarize_text(text: str) -> str:
    if not OPENAI_API_KEY:
        return "OpenAI API key is missing. Set the OPENAI_API_KEY environment variable."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Using GPT-4o mini for cost-effective summarization
            messages=[
                {"role": "system", "content": "You are a legal assistant."},
                {"role": "user", "content": f"Summarize this legal document:\n{text}"}
            ],
            temperature=0.3
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"
