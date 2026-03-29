import os
from langchain_community.vectorstores import FAISS
from logger import get_logger

logger = get_logger(__name__)

def create_vector_store(chunks, embeddings):
    """Create and save FAISS vector store from document chunks."""
    try:
        from config import FAISS_INDEX_PATH
        
        logger.info(f"Creating FAISS vector store with {len(chunks)} chunks...")
        vector_db = FAISS.from_documents(chunks, embeddings)
        
        # Create directory if it doesn't exist
        os.makedirs(FAISS_INDEX_PATH, exist_ok=True)
        
        vector_db.save_local(FAISS_INDEX_PATH)
        logger.info(f"FAISS index saved to {FAISS_INDEX_PATH}")
        
        return vector_db
    except Exception as e:
        logger.error(f"Error creating vector store: {str(e)}")
        raise

def load_vector_store(embeddings):
    """Load FAISS vector store for similarity search."""
    try:
        from config import FAISS_INDEX_PATH
        
        if not os.path.exists(FAISS_INDEX_PATH):
            raise FileNotFoundError(
                f"FAISS index not found at {FAISS_INDEX_PATH}. "
                f"Please run 'python scripts/create_index.py' first."
            )
        
        logger.info(f"Loading FAISS vector store...")
        db = FAISS.load_local(
            FAISS_INDEX_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
        logger.info("FAISS vector store loaded successfully")
        
        return db
    except FileNotFoundError as e:
        logger.error(str(e))
        raise
    except Exception as e:
        logger.error(f"Error loading vector store: {str(e)}")
        raise
        raise