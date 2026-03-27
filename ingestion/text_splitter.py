from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP
from logger import get_logger

logger = get_logger(__name__)

def split_documents(documents):
    """Split documents into chunks."""
    try:
        logger.info(f"Splitting {len(documents)} documents with chunk_size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP}...")
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        chunks = splitter.split_documents(documents)
        logger.info(f"Created {len(chunks)} chunks")
        
        return chunks
    except Exception as e:
        logger.error(f"Error splitting documents: {str(e)}")
        raise