import openai
import os

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str) -> str:
    """
    Summarizes a legal document using GPT-4o mini.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using GPT-4o mini as per the latest API docs
            messages=[
                {"role": "system", "content": "You are a legal assistant specialized in summarizing legal documents."},
                {"role": "user", "content": f"Please summarize this legal document:\n\n{text}"}
            ],
            temperature=0.3,
            max_tokens=300
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        return f"Error: {e}"
