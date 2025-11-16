@echo off
REM Computer Vision Project Setup Script for Windows
REM This script sets up the environment for the Computer Vision project

echo ==========================================
echo 🎥 Computer Vision Project Setup
echo ==========================================
echo.

REM Check if Python is installed
echo 📌 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

python --version
echo ✅ Python detected
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo ✅ Virtual environment created
) else (
    echo ℹ️  Virtual environment already exists
)
echo.

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated
echo.

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1
echo ✅ pip upgraded
echo.

REM Install requirements
echo 📥 Installing dependencies...
echo    This may take a few minutes...
pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo ❌ Error installing dependencies
    pause
    exit /b 1
)
echo ✅ Dependencies installed successfully
echo.

REM Create necessary directories
echo 📁 Creating project directories...
if not exist "models" mkdir models
if not exist "app\templates" mkdir app\templates
if not exist "app\static" mkdir app\static
if not exist "notebooks" mkdir notebooks
echo ✅ Directories created
echo.

REM Check if model exists
echo 🔍 Checking for trained model...
if exist "models\cifar10_model.h5" (
    echo ✅ Trained model found
) else (
    echo ⚠️  No trained model found
    echo    Please train the model using: notebooks/01_train_model.ipynb
)
echo.

echo ==========================================
echo ✅ Setup Complete!
echo ==========================================
echo.
echo 📚 Next Steps:
echo.
echo 1. Train the model:
echo    jupyter notebook notebooks/01_train_model.ipynb
echo.
echo 2. Run the web app:
echo    python app/app.py
echo.
echo 3. Or use Google Colab:
echo    Open notebooks/complete_colab_workflow.ipynb in Colab
echo.
echo 🚀 Happy Learning!
echo.
pause
