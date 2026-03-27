import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ingestion.pdf_loader import load_pdf_documents
from ingestion.text_splitter import split_documents
from ingestion.embedding_generator import load_embedding_model
from vector_db.vectordb import create_vector_store
from config import PDF_PATH
from logger import get_logger

logger = get_logger(__name__)

def create_faiss_index(pdf_path=None):
    """Create FAISS index from PDF."""
    try:
        if pdf_path is None:
            pdf_path = PDF_PATH
        
        logger.info(f"Creating FAISS index from: {pdf_path}")
        
        docs = load_pdf_documents(pdf_path)
        
        chunks = split_documents(docs)
        
        embeddings = load_embedding_model()
        
        create_vector_store(chunks, embeddings)
        
        logger.info("✓ FAISS index created successfully")
        return True
    except FileNotFoundError as e:
        logger.error(f"Error: PDF file not found - {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Error creating index: {str(e)}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create FAISS index from PDF documents")
    parser.add_argument(
        "--pdf-path",
        type=str,
        default=None,
        help=f"Path to PDF file (default: {PDF_PATH})"
    )
    
    args = parser.parse_args()
    
    success = create_faiss_index(args.pdf_path)
    sys.exit(0 if success else 1)