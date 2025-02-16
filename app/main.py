from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.summarizer import summarize_text
from app.qa_model import answer_question

app = FastAPI(
    title="AI-Powered Legal Assistant",
    description="Summarization & Legal Q&A API",
)

# Request body structure for summarization
class TextRequest(BaseModel):
    text: str

# Request body structure for legal Q&A
class QARequest(BaseModel):
    question: str
    context: str

@app.get("/")
def home():
    return {"message": "Welcome to the AI-Powered Legal Assistant API 🚀"}

@app.post("/summarize")
def summarize(request: TextRequest):
    try:
        summary = summarize_text(request.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask")
def legal_qa(request: QARequest):
    try:
        answer = answer_question(request.question, request.context)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
