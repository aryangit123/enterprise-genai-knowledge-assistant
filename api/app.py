from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import API_HOST, API_PORT
from rag_pipeline.main_rag_pipeline import rag_pipeline
from logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Enterprise GenAI Knowledge Assistant",
    description="RAG system for document-based question answering",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    """Query request model."""
    question: str

@app.get("/")
def root():
    """Health check endpoint."""
    logger.info("Health check called")
    return {
        "message": "Enterprise GenAI Knowledge Assistant API running",
        "status": "healthy"
    }

@app.post("/query")
def query_documents(request: QueryRequest):
    """Query documents endpoint."""
    try:
        if not request.question or not request.question.strip():
            logger.warning("Empty question received")
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )
        
        logger.info(f"Processing query: {request.question[:50]}...")
        answer = rag_pipeline(request.question)
        
        return {
            "question": request.question,
            "answer": answer
        }
    except FileNotFoundError as e:
        logger.error(f"FAISS index error: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail=f"Vector store not available: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        )

@app.get("/query")
def query_documents_get(question: str):
    """Query documents endpoint (GET method)."""
    try:
        if not question or not question.strip():
            logger.warning("Empty question received (GET)")
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )
        
        logger.info(f"Processing GET query: {question[:50]}...")
        answer = rag_pipeline(question)
        
        return {
            "question": question,
            "answer": answer
        }
    except FileNotFoundError as e:
        logger.error(f"FAISS index error: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail=f"Vector store not available: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting API server on {API_HOST}:{API_PORT}")
    uvicorn.run(app, host=API_HOST, port=API_PORT)