import streamlit as st
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_pipeline.main_rag_pipeline import rag_pipeline
from logger import get_logger

logger = get_logger(__name__)

# Page configuration
st.set_page_config(
    page_title="Enterprise GenAI Knowledge Assistant",
    page_icon="📚",
    layout="wide"
)

# Header
st.title("📚 Enterprise GenAI Knowledge Assistant")
st.write(
    "Ask questions about your documents. The system will find relevant information and provide answers."
)

# Sidebar information
with st.sidebar:
    st.header("ℹ️ How It Works")
    st.markdown("""
    ### The Process:
    1. **Input**: You ask a question
    2. **Search**: The system finds relevant parts of your documents
    3. **Answer**: An AI generates an answer based on the found information
    
    ### Required:
    - FAISS index must be built first
    - PDFs should be in `data/sample_pdfs/`
    """)

# Input box
query = st.text_input("Ask a question about your documents:")

# Submit button
if st.button("Search", type="primary"):
    if query.strip() == "":
        st.warning("⚠️ Please enter a question!")
    else:
        with st.spinner("🔍 Searching documents..."):
            try:
                logger.info(f"User query: {query}")
                answer = rag_pipeline(query)
                
                st.subheader("Answer:")
                st.success(answer)
                logger.info("Query success")
                
            except FileNotFoundError:
                st.error("❌ FAISS index not found!")
                st.info(
                    "Create the index first:\n```\npython scripts/create_index.py\n```"
                )
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("Make sure FAISS index is built: `python scripts/create_index.py`")
                logger.error(f"Error: {str(e)}")

st.markdown("---")
st.caption("Enterprise GenAI Knowledge Assistant")