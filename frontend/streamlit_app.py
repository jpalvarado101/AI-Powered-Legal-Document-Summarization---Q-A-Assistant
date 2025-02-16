import streamlit as st
import requests

# FastAPI Backend URL (adjust if needed when deployed)
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Legal AI Assistant", layout="wide")

st.title("📜 AI-Powered Legal Document Summarization & Q&A")
st.write("Upload a legal document to get an AI-generated summary, or ask legal questions!")

# Upload a legal document (text file)
uploaded_file = st.file_uploader("📂 Upload a Legal Document (Text Only)", type=["txt"])

if uploaded_file is not None:
    document_text = uploaded_file.read().decode("utf-8")

    st.subheader("📑 Document Preview")
    st.text_area("Uploaded Text:", document_text[:500] + "..." if len(document_text) > 500 else document_text, height=150)

    if st.button("🔍 Summarize Document"):
        with st.spinner("Generating AI Summary..."):
            response = requests.post(f"{API_URL}/summarize", json={"text": document_text})
            if response.status_code == 200:
                summary = response.json().get("summary", "No summary generated.")
                st.subheader("📌 AI-Generated Summary")
                st.success(summary)
            else:
                st.error("Error in summarization. Try again.")

# Legal Q&A Section
st.subheader("⚖️ Legal Question Answering")
question = st.text_input("Enter a legal question:")
context = st.text_area("Provide relevant legal text (optional):", "")

if st.button("🤖 Get AI Answer"):
    with st.spinner("Generating Answer..."):
        response = requests.post(f"{API_URL}/ask", json={"question": question, "context": context})
        if response.status_code == 200:
            answer = response.json().get("answer", "No answer found.")
            st.subheader("🧠 AI Response")
            st.info(answer)
        else:
            st.error("Error retrieving answer. Try again.")

st.markdown("---")
st.markdown("💡 Built with [FastAPI](https://fastapi.tiangolo.com/) & [Streamlit](https://streamlit.io/) | 🚀 Powered by GPT-4o mini")
