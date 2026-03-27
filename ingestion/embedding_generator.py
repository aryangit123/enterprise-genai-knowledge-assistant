from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL
from logger import get_logger

logger = get_logger(__name__)

def load_embedding_model():
    """Load embedding model."""
    try:
        logger.info(f"Loading embedding model: {EMBEDDING_MODEL}...")
        
        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )
        
        logger.info("Embedding model loaded successfully")
        return embeddings
    except Exception as e:
        logger.error(f"Error loading embedding model: {str(e)}")
        raise