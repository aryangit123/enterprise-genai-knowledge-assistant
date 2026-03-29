# 🧠 Enterprise GenAI Knowledge Assistant

> **RAG-powered document question-answering system** — extract insights from enterprise PDFs and technical reports using Retrieval-Augmented Generation, LLaMA, and a full MLOps pipeline.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.1.14-1C3C3C?style=flat-square&logo=chainlink&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=flat-square&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.37-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-2.13-0194E2?style=flat-square&logo=mlflow&logoColor=white)

---

## 📌 Overview

The **Enterprise GenAI Knowledge Assistant** is an end-to-end AI system that lets users query enterprise documents — technical PDFs, reports, manuals — using natural language. Built on **Retrieval-Augmented Generation (RAG)**, it combines semantic search over a FAISS vector store with a locally-hosted LLaMA language model to deliver grounded, source-cited answers in real time.

The system is production-ready with a REST API (FastAPI), an interactive UI (Streamlit), Docker-based containerization, and MLflow experiment tracking.

---

## ✨ Key Features

- **Document Ingestion Pipeline** — Parses PDFs, applies semantic chunking, generates embeddings, and stores them in a FAISS index
- **Semantic Retrieval** — Uses `sentence-transformers` to find the most relevant document chunks for any user query
- **Context-Aware Answer Generation** — Integrates LLaMA models via HuggingFace Transformers for grounded, source-cited responses
- **REST API** — FastAPI endpoints for programmatic querying, suitable for integration into enterprise applications
- **Interactive UI** — Streamlit interface for real-time document Q&A without any API knowledge required
- **MLOps Integration** — MLflow tracks experiments, model parameters, and pipeline runs for reproducibility and monitoring
- **Containerized Deployment** — Docker Compose setup to spin up the full stack (API + UI + MLflow) with a single command

---

## 🏗️ Architecture

```
User Query
    │
    ▼
┌─────────────────────────────────────────────┐
│              Document Ingestion              │
│  PDF Parsing → Chunking → Embeddings → FAISS│
└─────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────┐
│              RAG Pipeline                    │
│  Query Embedding → Semantic Retrieval        │
│  → Context Assembly → LLaMA Generation      │
└─────────────────────────────────────────────┘
    │
    ├──► FastAPI (REST API)   → http://localhost:8000
    ├──► Streamlit (UI)       → http://localhost:8501
    └──► MLflow (Monitoring)  → http://localhost:5000
```

---

## 🗂️ Project Structure

```
enterprise-genai-knowledge-assistant/
├── api/                    # FastAPI REST endpoints
├── ui/                     # Streamlit interactive interface
├── rag_pipeline/           # Core RAG logic (retrieval + generation)
├── ingestion/              # PDF parsing and chunking
├── vector_db/              # FAISS vector store management
├── mlops/                  # MLflow tracking and monitoring
├── scripts/                # Utility scripts (e.g., create_index.py)
├── docker/                 # Dockerfiles for each service
├── data/sample_pdfs/       # Input PDF documents
├── faiss_index/            # Persisted FAISS vector index
├── config.py               # Centralized configuration
├── logger.py               # Logging utilities
├── docker-compose.yml      # Multi-service container orchestration
├── requirements.txt        # Python dependencies
├── setup.sh                # Linux/Mac setup script
├── setup.bat               # Windows setup script
├── .env.example            # Environment variable template
└── QUICKSTART.md           # Fast setup guide
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| RAG Framework | LangChain |
| Vector Store | FAISS |
| Embeddings | HuggingFace `sentence-transformers` |
| LLM | LLaMA (via HuggingFace Transformers) |
| API | FastAPI + Uvicorn |
| UI | Streamlit |
| Containerization | Docker + Docker Compose |
| Experiment Tracking | MLflow |
| PDF Parsing | PyPDF |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (optional, for containerized setup)
- 8GB+ RAM recommended for local LLM inference

### 1. Clone the Repository

```bash
git clone https://github.com/aryangit123/enterprise-genai-knowledge-assistant.git
cd enterprise-genai-knowledge-assistant
```

### 2. Setup Environment

**Linux/Mac:**
```bash
bash setup.sh
```

**Windows:**
```bat
setup.bat
```

**Manual setup:**
```bash
python -m venv genai_env
source genai_env/bin/activate      # Linux/Mac
# genai_env\Scripts\activate       # Windows

pip install -r requirements.txt
cp .env.example .env
```

### 3. Configure Environment Variables

Edit the `.env` file to set your models and preferences:

```env
# Embedding Model
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# LLM Model
LLM_MODEL=TinyLlama/TinyLlama-1.1B-Chat-v1.0
LLM_MAX_TOKENS=300
LLM_TEMPERATURE=0.7

# Retrieval
RETRIEVAL_K=3

# API
API_PORT=8000

# Device (0 for GPU, -1 for CPU)
LLM_DEVICE=-1
```

### 4. Index Your Documents

Place PDFs in `data/sample_pdfs/` and build the FAISS index:

```bash
python scripts/create_index.py --pdf-path data/sample_pdfs/your_document.pdf
```

### 5. Run the Application

**Streamlit UI (recommended):**
```bash
streamlit run ui/streamlit_app.py
# → http://localhost:8501
```

**FastAPI Server:**
```bash
uvicorn api.app:app --reload
# → http://localhost:8000
```

**Example API call:**
```bash
curl "http://localhost:8000/query?question=What%20are%20the%20key%20findings?"
```

**Full Docker stack (API + UI + MLflow):**
```bash
docker-compose up
```

| Service | URL |
|---|---|
| Streamlit UI | http://localhost:8501 |
| FastAPI | http://localhost:8000 |
| MLflow Dashboard | http://localhost:5000 |

---

## 📊 MLflow Monitoring

Track experiment runs, retrieval parameters, and model configurations:

```bash
mlflow ui
# → http://localhost:5000
```

All RAG pipeline executions are automatically logged — including embedding model, LLM config, retrieval K, and response metadata.

---

## 🔧 Troubleshooting

| Issue | Solution |
|---|---|
| `FAISS index not found` | Run `python scripts/create_index.py` |
| `PDF not found` | Place PDFs in `data/sample_pdfs/` and verify path in `.env` |
| `Module not found` | Re-activate the venv and run `pip install -r requirements.txt` |
| `Out of Memory` | Reduce `LLM_MAX_TOKENS` or set `LLM_DEVICE=-1` for CPU mode |

---

## 🧩 How It Works

1. **Ingestion** — PDFs are parsed with PyPDF, split into semantic chunks using LangChain's text splitters, and embedded with `sentence-transformers`.
2. **Indexing** — Embeddings are stored in a FAISS vector index for fast approximate nearest-neighbor search.
3. **Retrieval** — At query time, the user's question is embedded and the top-K most semantically similar chunks are retrieved from FAISS.
4. **Generation** — The retrieved chunks are assembled into a context window and passed to a LLaMA model (via HuggingFace Transformers) to generate a grounded, source-cited answer.
5. **Serving** — Answers are delivered via Streamlit UI or FastAPI REST endpoint, with all runs tracked in MLflow.

---

## 📄 License

This project is open-source. See [LICENSE](LICENSE) for details.

---

## 🙋 Author

**Aryan** — [GitHub](https://github.com/aryangit123)
