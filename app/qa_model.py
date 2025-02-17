import openai
import os

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer_question(question: str, context: str) -> str:
    """
    Answers a legal question based on provided context using GPT-4o mini.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using GPT-4o mini for cost-effective legal Q&A
            messages=[
                {"role": "system", "content": "You are a legal expert who provides concise and precise answers."},
                {"role": "user", "content": f"Question: {question}\nContext: {context}"}
            ],
            temperature=0.3,
            max_tokens=200
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return f"Error: {e}"
