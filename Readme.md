# **📜 AI-Powered Legal Document Summarization & Q&A Assistant**  

![Legal AI Assistant]() 

**🔍 Summary**  
AI-powered tool that automates legal document summarization and provides legal Q&A assistance using **GPT-4o mini** and **Natural Language Processing (NLP)**. This project helps legal professionals save time by extracting key insights from contracts, case files, and other legal documents at a **low cost**.  

🚀 **Live Demo: coming soon** <!-- [Link to Deployed App] *(if available)*   -->
🛠 **Tech Stack:** Python | FastAPI | GPT-4o mini | Streamlit | Docker | AWS/GCP/Hugging Face Spaces  

---

## **📌 Features**
✅ **Legal Document Summarization** – Extracts key insights from long legal texts  
✅ **Legal Q&A Assistant** – Answers legal-related questions using AI  
✅ **GPT-4o mini Model** – Cost-effective, powerful LLM  
✅ **FastAPI Backend** – Exposes API endpoints for easy integration  
✅ **Streamlit UI** – Upload legal documents and get instant summaries  
✅ **Cloud Deployment** – Runs on AWS/GCP/Hugging Face Spaces  

---

## **🚀 Quick Start Guide**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/legal-ai-assistant.git
cd legal-ai-assistant
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up API Keys**
```bash
export OPENAI_API_KEY="your-api-key"
```

### **4️⃣ Run the FastAPI Backend**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Now, your API is running on **`http://127.0.0.1:8000/docs`** 🚀  

### **5️⃣ Run the Streamlit UI**
```bash
streamlit run frontend/streamlit_app.py
```
This launches a web app where you can upload legal documents for summarization.  

---

## **📡 API Endpoints**
### **1️⃣ Summarization Endpoint**
**Request:**  
```json
POST /summarize
{
  "text": "Full legal document text here"
}
```
**Response:**  
```json
{
  "summary": "Key points extracted from the legal document..."
}
```

### **2️⃣ Legal Q&A Endpoint**
**Request:**  
```json
POST /ask
{
  "question": "What is a breach of contract?",
  "context": "Relevant legal text here"
}
```
**Response:**  
```json
{
  "answer": "A breach of contract occurs when..."
}
```

---

## **📂 Project Structure**
```
📁 legal-ai-assistant
│── 📂 app
│   ├── main.py                # FastAPI app
│   ├── summarizer.py          # GPT-4o mini for document summarization
│   ├── qa_model.py            # GPT-4o mini for legal Q&A
│   ├── utils.py               # Helper functions
│── 📂 frontend
│   ├── streamlit_app.py        # Streamlit UI
│── requirements.txt           # Dependencies
│── Dockerfile                 # Deployment config
│── README.md                  # Project documentation
│── .gitignore                 # Ignoring unnecessary files
```

---

## **💰 Cost Efficiency**
Using **GPT-4o mini**, the cost per **one-page (500-word) document** is:  
📜 **Summarization:** **$0.000195** (~0.02 cents)  
⚖️ **Q&A Answer:** **$0.0001425** (~0.01 cents)  
🚀 **Total per document:** **~$0.00034** (~0.03 cents)  

---

## **📦 Deployment**
### **1️⃣ Docker Setup**
```bash
docker build -t legal-ai-assistant .
docker run -p 8000:8000 legal-ai-assistant
```

### **2️⃣ Cloud Deployment**
- Deploy FastAPI backend on **AWS/GCP/Hugging Face Spaces**  
- Use **Streamlit Cloud** for UI  

---

## **📚 Future Improvements**
✅ **Fine-tune GPT-4o mini on legal datasets**  
✅ **Enhance legal text retrieval with RAG (Retrieval-Augmented Generation)**  
✅ **Integrate Speech-to-Text for lawyer-client meeting transcriptions**  

---

## **🙌 Contributing**
Want to improve this project? Contributions are welcome!  

```bash
git checkout -b feature-branch
git commit -m "Add new feature"
git push origin feature-branch
```

---

## **📜 License**
This project is licensed under the **MIT License**.  

---

## **🔗 Connect with Me**
📧 Email: contact@johnferreralvarado.com

💼 LinkedIn: [johnfalvarado](https://www.linkedin.com/in/johnfalvarado/) 
 
🌎 Portfolio: [JohnFerrerAlvarado.com](https://johnferreralvarado.com/)  

---

### **🔥 Final Thoughts**
With this **AI-Powered Legal Assistant**, you’re **directly showcasing LLM, NLP, and MLOps skills** that align **perfectly** with Clio’s job description. **Deploying this and sharing it on your resume & LinkedIn will boost your hiring chances massively.** 🚀  

**Next Steps:**  
- Let me know if you need **GitHub setup support** or **deployment assistance**! 🎯🔥

