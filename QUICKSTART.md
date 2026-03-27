# Quick Start Guide

## 🚀 Fast Setup (5 minutes)

### Option 1: Direct Installation

**Windows:**
```bash
setup.bat
```

**Linux/Mac:**
```bash
bash setup.sh
```

### Option 2: Manual Setup

1. **Create and activate virtual environment:**
   ```bash
   # Windows
   python -m venv genai_env
   genai_env\Scripts\activate
   
   # Linux/Mac
   python -m venv genai_env
   source genai_env/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Copy environment file:**
   ```bash
   # Windows
   copy .env.example .env
   
   # Linux/Mac
   cp .env.example .env
   ```

---

## 📄 Create FAISS Index

Before running the app, you need to create the FAISS index from your PDF documents.

1. **Place your PDF in `data/sample_pdfs/` directory**

2. **Run the indexing script:**
   ```bash
   python scripts/create_index.py --pdf-path data/sample_pdfs/sample.pdf
   ```

   Or use the default path from config:
   ```bash
   python scripts/create_index.py
   ```

---

## 🎯 Run the Application

### Option 1: Streamlit UI (Recommended for Users)

```bash
streamlit run ui/streamlit_app.py
```

Access at: `http://localhost:8501`

### Option 2: FastAPI Server

```bash
uvicorn api.app:app --reload
```

Access at: `http://localhost:8000`

Test endpoint:
```bash
curl "http://localhost:8000/query?question=What%20is%20the%20company%20policy?"
```

### Option 3: Docker (All-in-One)

**Streamlit:**
```bash
docker-compose up streamlit
```

**FastAPI:**
```bash
docker-compose up fastapi
```

**Both + MLflow:**
```bash
docker-compose up
```

---

## 🔧 Configuration

Edit `.env` file to customize:

```env
# Embedding Model
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# LLM Model
LLM_MODEL=TinyLlama/TinyLlama-1.1B-Chat-v1.0
LLM_MAX_TOKENS=300
LLM_TEMPERATURE=0.7

# Retrieval
RETRIEVAL_K=3

# API Port
API_PORT=8000
```

---

## 🐛 Troubleshooting

### "FAISS index not found"
- Run: `python scripts/create_index.py`
- Check that `faiss_index/` directory exists

### "PDF not found"
- Verify PDF path in `.env` or script parameter
- Place PDFs in `data/sample_pdfs/`

### "Module not found"
- Reactivate virtual environment: `source genai_env/bin/activate` (or `.bat` on Windows)
- Reinstall: `pip install -r requirements.txt`

### "Out of Memory"
- Reduce `LLM_MAX_TOKENS` in `.env`
- Use CPU only: Set `LLM_DEVICE=-1`
- For GPU: Set `LLM_DEVICE=0` (requires CUDA)

---

## 📊 Monitor with MLflow

```bash
mlflow ui
```

Access at: `http://localhost:5000`

---

## 📚 Project Structure

```
.
├── api/                      # FastAPI endpoints
├── ui/                       # Streamlit interface
├── rag_pipeline/            # RAG core logic
├── ingestion/               # PDF processing
├── vector_db/               # FAISS vector store
├── scripts/                 # Utility scripts
├── data/sample_pdfs/        # Input PDFs
├── faiss_index/             # Embedded vectors
├── docker/                  # Docker setup
├── config.py                # Configuration
├── requirements.txt         # Dependencies
└── README.md               # Full documentation
```

---

## 🎓 Example Query

```
Question: "What are the key policies?"
Response: "Based on the document, the key policies include..."
```

---

## 📞 Support

See full `README.md` for detailed documentation and troubleshooting.
