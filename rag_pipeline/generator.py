from transformers import pipeline
from config import LLM_MODEL, LLM_MAX_TOKENS, LLM_TEMPERATURE, LLM_TOP_P, LLM_DEVICE
from logger import get_logger

logger = get_logger(__name__)

# Global cache for the generator model
_generator_cache = None

def get_generator():
    """Get or create generator instance (cached)."""
    global _generator_cache
    
    if _generator_cache is None:
        try:
            logger.info(f"Loading LLM model: {LLM_MODEL} (device: {LLM_DEVICE})")
            _generator_cache = pipeline(
                task="text-generation",
                model=LLM_MODEL,
                max_new_tokens=LLM_MAX_TOKENS,
                device=LLM_DEVICE
            )
            logger.info("LLM model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading LLM model: {str(e)}")
            raise
    
    return _generator_cache

def generate_answer(prompt: str) -> str:
    """Generate answer from the language model."""
    try:
        logger.info("Generating answer...")
        generator = get_generator()
        
        result = generator(
            prompt,
            do_sample=True,
            temperature=LLM_TEMPERATURE,
            top_p=LLM_TOP_P
        )

        generated_text = result[0]["generated_text"]

        # Remove prompt from generated text
        answer = generated_text.replace(prompt, "").strip()
        
        logger.info("Answer generated successfully")
        return answer
    except Exception as e:
        logger.error(f"Error generating answer: {str(e)}")
        raise