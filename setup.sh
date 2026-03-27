#!/bin/bash
# Enterprise GenAI Knowledge Assistant - Setup Script

echo "=================================="
echo "Enterprise GenAI Setup"
echo "=================================="

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python installation
echo -e "${BLUE}[1/5]${NC} Checking Python installation..."
if ! command -v python &> /dev/null; then
    echo -e "${YELLOW}Python not found. Please install Python 3.10+${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python found$(python --version)${NC}"

# Create virtual environment if not exists
echo -e "${BLUE}[2/5]${NC} Setting up virtual environment..."
if [ ! -d "genai_env" ]; then
    python -m venv genai_env
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "${BLUE}[3/5]${NC} Activating virtual environment..."
source genai_env/bin/activate 2>/dev/null || genai_env\Scripts\activate 2>/dev/null
echo -e "${GREEN}✓ Virtual environment activated${NC}"

# Install dependencies
echo -e "${BLUE}[4/5]${NC} Installing dependencies..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"

# Create .env file if not exists
echo -e "${BLUE}[5/5]${NC} Setting up configuration..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo -e "${GREEN}✓ .env file created from template${NC}"
else
    echo -e "${GREEN}✓ .env file already exists${NC}"
fi

echo ""
echo "=================================="
echo -e "${GREEN}Setup completed successfully!${NC}"
echo "=================================="
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Create FAISS index: python scripts/create_index.py --pdf-path data/sample_pdfs/sample.pdf"
echo "2. Run Streamlit UI: streamlit run ui/streamlit_app.py"
echo "3. Or run FastAPI: uvicorn api.app:app --reload"
echo ""
echo -e "${YELLOW}Docker option:${NC}"
echo "docker-compose up -d streamlit"
echo ""
