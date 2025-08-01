@echo off
echo ========================================
echo    HackaAIverse 2024 - Startup Script
echo ========================================
echo.

echo [1/3] Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found! Please install Python 3.8+
    pause
    exit /b 1
)

echo [2/3] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)

echo [3/3] Starting HackaAIverse application...
echo.
echo ========================================
echo   Application will open in your browser
echo   URL: http://localhost:8501
echo   Admin Password: author@123
echo ========================================
echo.
echo Press Ctrl+C to stop the application
echo.

streamlit run project.py

pause
