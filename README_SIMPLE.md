# 📚 Enterprise GenAI Knowledge Assistant

A simple Python project that lets you ask questions about your PDF documents and get answers powered by AI.

---

## 🎯 What Does It Do?

1. **Read PDFs** - Loads and processes your documents
2. **Find Answers** - Searches for relevant information based on your question
3. **Generate Responses** - Uses AI to create natural answers

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install

```bash
# Create virtual environment
python -m venv genai_env

# Activate it
genai_env\Scripts\activate  # Windows
source genai_env/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Create Index

```bash
# This reads your PDFs and creates a searchable index
python scripts/create_index.py
```

### Step 3: Run

**Option A: Web Interface (Easiest)**
```bash
streamlit run ui/streamlit_app.py
# Opens at http://localhost:8501
```

**Option B: REST API**
```bash
python api/app.py
# API at http://localhost:8000

# Test it:
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is this document about?"}'
```

---

## 📁 Project Structure

```
project/
├── data/
│   └── sample_pdfs/          # Put your PDFs here
├── ingestion/                # Reads & processes PDFs
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   └── embedding_generator.py
├── vector_db/                # Stores searchable data
│   └── vectordb.py
├── rag_pipeline/             # Finds answers
│   ├── main_rag_pipeline.py  # Main logic
│   ├── retriever.py          # Finds similar documents
│   ├── generator.py          # Generates answers
│   └── prompt.py             # Creates prompts
├── api/                      # REST API
│   └── app.py
├── ui/                       # Web interface
│   └── streamlit_app.py
├── scripts/
│   └── create_index.py       # Creates searchable index
├── config.py                 # Settings
├── logger.py                 # Logging
└── requirements.txt          # Dependencies
```

---

## 💻 How It Works

### Simple Explanation:

1. **Embedding** - Convert text to numbers (vectors) that computers can understand
2. **Indexing** - Store these vectors in a searchable database (FAISS)
3. **Retrieval** - Find documents similar to the user's question
4. **Generation** - Use AI (LLaMA) to create an answer from the found documents

### Technical Flow:

```
User Question
    ↓
Embed to vectors (All-MiniLM-L6-v2)
    ↓
Search in FAISS index
    ↓
Get top 3 similar documents
    ↓
Create prompt with documents + question
    ↓
LLM generates answer (TinyLlama)
    ↓
Return answer to user
```

---

## 🔧 Configuration

Edit `.env` file to customize:

```env
# Which embedding model to use
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Which LLM to use  
LLM_MODEL=TinyLlama/TinyLlama-1.1B-Chat-v1.0

# How many documents to search
RETRIEVAL_K=3

# API port
API_PORT=8000
```

---

## 🐛 Troubleshooting

### "FAISS index not found"
```bash
python scripts/create_index.py
```

### "PDF not found"
- Put PDFs in `data/sample_pdfs/`
- Update `PDF_PATH` in `.env` if using different location

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Out of Memory"
Reduce `LLM_MAX_TOKENS` in `.env` from 300 to 150

---

## 📚 Model Information

| Component | Model | Size | Speed |
|-----------|-------|------|-------|
| Embedding | all-MiniLM-L6-v2 | 22 MB | Fast ⚡ |
| LLM (Answer Generation) | TinyLlama-1.1B | 1.1 B params | Fast ⚡ |
| Vector Store | FAISS | In-memory | Instant ⚡ |

---

## 🎯 Example Usage

### Web UI
1. Open http://localhost:8501
2. Put a question in the text box
3. Click "Search"
4. See the AI-generated answer

### REST API

```bash
# Single question
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the main topic?"}'

# Using GET
curl "http://localhost:8000/query?question=What%20is%20this%20about?"

# Health check
curl http://localhost:8000/
```

---

## 📝 Step-by-Step Guide

### 1. Prepare PDFs
- Create `data/sample_pdfs/` folder
- Put your PDF files there

### 2. Build Index
```bash
python scripts/create_index.py
```
This creates `faiss_index/` with searchable vectors

### 3. Ask Questions
- Via Web: `streamlit run ui/streamlit_app.py`
- Via API: `python api/app.py` then use curl/Python requests

---

## 🤝 How It Helps (Use Cases)

- 📋 Document Q&A - Ask questions about company documents
- 🎓 Learning - Understand technical papers
- 📖 Support - Provide instant answers from manuals
- 🔍 Search - Better document searching than full-text

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **ML Framework:** LangChain
- **Embeddings:** Sentence Transformers
- **Vector DB:** FAISS (Facebook AI Similarity Search)
- **LLM:** TinyLlama (fast, lightweight)
- **Web API:** FastAPI
- **Web UI:** Streamlit

---

## 📦 System Requirements

- Python 3.8 or higher
- 4GB+ RAM (8GB recommended)
- 2GB+ disk space for models

---

## 💡 Common Settings

### For Faster Responses
```env
RETRIEVAL_K=2          # Get fewer documents
LLM_MAX_TOKENS=150     # Shorter answers
CHUNK_SIZE=200         # Smaller chunks
```

### For Better Answers
```env
RETRIEVAL_K=5          # Get more documents
LLM_MAX_TOKENS=300     # Longer answers
CHUNK_SIZE=500         # Larger chunks
```

---

## 🚀 Next Steps

1. ✅ Install & run the basic project
2. 📄 Add your own PDFs to `data/sample_pdfs/`
3. 🔄 Rebuild index: `python scripts/create_index.py`
4. ❓ Ask questions and get answers
5. ⚙️ Adjust settings in `.env` for your needs

---

## 📞 Support

1. **Check logs:** `tail -f logs/app.log`
2. **Verify setup:** 
   - PDFs in `data/sample_pdfs/` ✓
   - Index created ✓
   - Dependencies installed ✓
3. **Read error messages** - They usually tell you what's wrong

---

## 🎓 For Beginners

This project teaches:
- 🤖 How RAG works
- 📊 Vector databases (FAISS)
- 🧠 Embeddings & similarity search
- 🦙 Using Language Models
- 🌐 Building APIs with FastAPI
- 🎨 Building UIs with Streamlit

---

## 📝 Notes

- First run takes longer (downloads models)
- Subsequent runs are faster
- Models are cached after first download
- Internet required for first setup

---

**Enjoy querying your documents! 📚**
