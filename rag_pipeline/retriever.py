from config import RETRIEVAL_K
from logger import get_logger

logger = get_logger(__name__)

def retrieve_documents(query, vector_db, k=None):
    """Retrieve relevant documents from vector store."""
    if k is None:
        k = RETRIEVAL_K
    
    try:
        logger.info(f"Retrieving top {k} documents...")
        docs = vector_db.similarity_search(query, k=k)
        logger.info(f"Retrieved {len(docs)} documents")
        
        return docs
    except Exception as e:
        logger.error(f"Error retrieving documents: {str(e)}")
        raise