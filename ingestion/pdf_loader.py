from langchain_community.document_loaders import PyPDFLoader
from logger import get_logger

logger = get_logger(__name__)

def load_pdf_documents(pdf_path):
    """Load PDF documents."""
    try:
        logger.info(f"Loading PDF from: {pdf_path}")
        
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        
        logger.info(f"Successfully loaded {len(documents)} pages from PDF")
        return documents
    except FileNotFoundError:
        logger.error(f"PDF file not found at: {pdf_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading PDF: {str(e)}")
        raise