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
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 Enterprise GenAI Knowledge Assistant")
st.write(
    "Ask questions from your enterprise documents (PDFs). "
    "The system will retrieve relevant context and generate answers."
)

# Sidebar information
with st.sidebar:
    st.header("ℹ️ Information")
    st.markdown("""
    ### How it works:
    1. **Ingestion**: PDFs are processed and converted to embeddings
    2. **Retrieval**: Relevant documents are fetched for your query
    3. **Generation**: An answer is generated based on the context
    
    ### Requirements:
    - FAISS index must be built before querying
    - PDFs should be in `data/sample_pdfs/`
    """)

# Input box
query = st.text_input("Enter your question here:")

# Submit button
if st.button("Submit", type="primary"):
    if query.strip() == "":
        st.warning("⚠️ Please enter a valid question!")
    else:
        with st.spinner("🔍 Retrieving information and generating answer..."):
            try:
                logger.info(f"Processing query from UI: {query[:100]}")
                answer = rag_pipeline(query)
                st.subheader("💡 Answer:")
                st.success(answer)
                logger.info("Query processed successfully")
            except FileNotFoundError as e:
                st.error(f"❌ FAISS index not found!")
                st.info(
                    "Please create the FAISS index first by running:\n"
                    "`python scripts/create_index.py`\n\n"
                    "Make sure your PDF is in `data/sample_pdfs/` directory."
                )
                logger.error(f"FAISS index error: {str(e)}")
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info(
                    "Common solutions:\n"
                    "1. Verify FAISS index is built: `python scripts/create_index.py`\n"
                    "2. Check PDF file exists in `data/sample_pdfs/`\n"
                    "3. Verify all models are properly installed"
                )
                logger.error(f"Error in UI: {str(e)}")

# Optional: Footer
st.markdown("---")
st.caption("Enterprise GenAI Knowledge Assistant | MTech Project Demo")