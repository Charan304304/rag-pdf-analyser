# 📄 RAG PDF Analyser

An AI-powered application to **chat with multiple PDF documents** using Retrieval-Augmented Generation (RAG).
Upload PDFs, ask questions, and get accurate answers along with **source page references**.

---

## 🚀 Features

* 📄 Upload and process multiple PDF files
* 🤖 Ask questions based on document content
* 🧠 Uses FAISS for semantic search
* 🔍 Returns **relevant answers with source page numbers**
* 💬 ChatGPT-style UI with chat bubbles
* 🗂️ Supports large documents via chunking
* ⚡ Works offline using local LLM (no API dependency)

---

## 🏗️ Architecture

```
PDFs → Text Extraction → Chunking → Embeddings → FAISS → Query → LLM → Answer + Source
```

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Vector Store:** FAISS
* **Embeddings:** HuggingFace (sentence-transformers)
* **LLM:** FLAN-T5 (local model)
* **PDF Processing:** PyPDF2

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-pdf-analyser.git
cd rag-pdf-analyser
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 How to Use

1. Upload one or more PDF files
2. Click **Process**
3. Ask questions like:

   * "Summarize the document"
   * "What is the revenue?"
   * "Key highlights of the report"

---

## 📸 Sample Output

```
You: What is revenue?
Bot: The revenue is ₹500 Cr

📄 Source Pages: [12, 13]
```

---

## 🔐 Environment Variables (Optional)

If using API-based models:

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

> ⚠️ Do NOT upload `.env` to GitHub

---

## 🌐 Deployment

Deployed using Streamlit Cloud:

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect repo and deploy

---

## 🎯 Key Highlights

* Implements **RAG (Retrieval-Augmented Generation)**
* Handles **multi-document querying**
* Ensures **answer transparency with source tracking**
* Fully **deployable and scalable architecture**

---

## 📚 Future Enhancements

* 📄 PDF preview with highlighted answers
* 🧾 Multi-document comparison
* 📊 Financial data extraction
* 🌐 Integration with cloud LLMs

---

## 👨‍💻 Author

**Charan Simhadri**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
