@echo off
REM Setup script for Windows
REM This script automates the setup process for reviewers

echo ==========================================
echo Setting up cvds-debugging-exercises
echo ==========================================

REM Check Python version
echo Checking Python version...
python --version || python3 --version || (
    echo Error: Python 3 is required but not found
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv || python3 -m venv venv
) else (
    echo Virtual environment already exists
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

echo.
echo ==========================================
echo Setup complete!
echo ==========================================
echo.
echo To run all exercises, use:
echo   venv\Scripts\activate
echo   python run_all_exercises.py
echo.

pause

