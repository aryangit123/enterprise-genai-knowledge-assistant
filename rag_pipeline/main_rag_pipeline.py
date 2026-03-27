from ingestion.embedding_generator import load_embedding_model
from vector_db.vectordb import load_vector_store
from rag_pipeline.retriever import retrieve_documents
from rag_pipeline.prompt import build_prompt
from rag_pipeline.generator import generate_answer
from logger import get_logger

logger = get_logger(__name__)

def rag_pipeline(query):
    """Execute RAG pipeline."""
    try:
        logger.info(f"Starting RAG pipeline for query: {query[:100]}...")
        
        embeddings = load_embedding_model()

        vector_db = load_vector_store(embeddings)

        docs = retrieve_documents(query, vector_db)

        context = "\n".join([doc.page_content for doc in docs])

        prompt = build_prompt(context, query)

        answer = generate_answer(prompt)
        
        logger.info("RAG pipeline completed successfully")
        return answer
    except Exception as e:
        logger.error(f"Error in RAG pipeline: {str(e)}")
        raise