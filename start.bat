@echo off
REM Test Data Generator - Quick Start Script for Windows

echo ========================================
echo Test Data Generator - Quick Start
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please download Python from https://python.org/downloads/
    pause
    exit /b 1
)

echo Step 1: Installing dependencies...
pip install fastapi uvicorn >nul 2>&1
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    echo Try running: pip install fastapi uvicorn
    pause
    exit /b 1
)

echo.
echo Step 2: Starting server...
echo.
echo The app will be available at: http://127.0.0.1:8000
echo Press Ctrl+C to stop the server when done.
echo.
echo ========================================
echo.

REM Start the server
python -m uvicorn main:app --host 127.0.0.1 --port 8000

pause
