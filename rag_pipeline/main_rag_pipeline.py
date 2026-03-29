from ingestion.embedding_generator import load_embedding_model
from vector_db.vectordb import load_vector_store
from rag_pipeline.retriever import retrieve_documents
from rag_pipeline.prompt import build_prompt
from rag_pipeline.generator import generate_answer
from logger import get_logger

logger = get_logger(__name__)

def rag_pipeline(query):
    """Execute RAG pipeline to answer document questions."""
    try:
        logger.info(f"Processing query: {query[:50]}...")
        
        # 1. Load embedding model
        embeddings = load_embedding_model()
        
        # 2. Load vector store
        vector_db = load_vector_store(embeddings)
        
        # 3. Retrieve relevant documents
        docs = retrieve_documents(query, vector_db)
        
        # 4. Build context from retrieved documents
        context = "\n".join([doc.page_content for doc in docs])
        
        # 5. Create prompt with context
        prompt = build_prompt(context, query)
        
        # 6. Generate answer
        answer = generate_answer(prompt)
        
        logger.info("Query completed successfully")
        return answer
    except Exception as e:
        logger.error(f"Error in RAG pipeline: {str(e)}")
        raise