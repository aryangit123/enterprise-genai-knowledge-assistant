FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create logs directory
RUN mkdir -p logs

# Expose ports
# 8501 for Streamlit
# 8000 for FastAPI
EXPOSE 8501 8000

# Create entrypoint script
RUN echo '#!/bin/bash\n\
if [ "$1" = "api" ]; then\n\
    echo "Starting FastAPI server..."\n\
    uvicorn api.app:app --host 0.0.0.0 --port 8000\n\
elif [ "$1" = "streamlit" ]; then\n\
    echo "Starting Streamlit app..."\n\
    streamlit run ui/streamlit_app.py\n\
else\n\
    echo "Usage: docker run genai-assistant [api|streamlit]"\n\
    echo "Example: docker run -p 8501:8501 genai-assistant streamlit"\n\
    exit 1\n\
fi' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["streamlit"]