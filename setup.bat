@echo off
REM Enterprise GenAI Knowledge Assistant - Setup Script for Windows

echo ==================================
echo Enterprise GenAI Setup
echo ==================================

REM Check Python installation
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please install Python 3.10+
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version') do set "PYTHON_VERSION=%%i"
echo [OK] Python found: %PYTHON_VERSION%

REM Create virtual environment if not exists
echo [2/5] Setting up virtual environment...
if not exist "genai_env" (
    python -m venv genai_env
    echo [OK] Virtual environment created
) else (
    echo [OK] Virtual environment already exists
)

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call genai_env\Scripts\activate.bat
echo [OK] Virtual environment activated

REM Install dependencies
echo [4/5] Installing dependencies...
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
echo [OK] Dependencies installed

REM Create .env file if not exists
echo [5/5] Setting up configuration...
if not exist ".env" (
    copy .env.example .env
    echo [OK] .env file created from template
) else (
    echo [OK] .env file already exists
)

echo.
echo ==================================
echo Setup completed successfully!
echo ==================================
echo.
echo Next steps:
echo 1. Create FAISS index: python scripts\create_index.py --pdf-path data\sample_pdfs\sample.pdf
echo 2. Run Streamlit UI: streamlit run ui\streamlit_app.py
echo 3. Or run FastAPI: uvicorn api.app:app --reload
echo.
echo Docker option:
echo docker-compose up -d streamlit
echo.
pause
