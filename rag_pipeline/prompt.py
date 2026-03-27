from logger import get_logger

logger = get_logger(__name__)

def build_prompt(context, query):
    """Build prompt for the LLM."""
    try:
        prompt = f"""
You are an enterprise knowledge assistant.

Use ONLY the provided context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""
        logger.info("Prompt built successfully")
        return prompt
    except Exception as e:
        logger.error(f"Error building prompt: {str(e)}")
        raise