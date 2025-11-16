#!/bin/bash

# Computer Vision Project Setup Script
# This script sets up the environment for the Computer Vision project

echo "=========================================="
echo "🎥 Computer Vision Project Setup"
echo "=========================================="
echo ""

# Check Python version
echo "📌 Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+' | head -1)
required_version="3.8"

if (( $(echo "$python_version < $required_version" | bc -l) )); then
    echo "❌ Error: Python 3.8+ is required. You have Python $python_version"
    exit 1
fi

echo "✅ Python $python_version detected"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "ℹ️  Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✅ pip upgraded"
echo ""

# Install requirements
echo "📥 Installing dependencies..."
echo "   This may take a few minutes..."
pip install -r requirements.txt > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Error installing dependencies"
    exit 1
fi
echo ""

# Create necessary directories
echo "📁 Creating project directories..."
mkdir -p models app/templates app/static notebooks
echo "✅ Directories created"
echo ""

# Check if model exists
echo "🔍 Checking for trained model..."
if [ -f "models/cifar10_model.h5" ]; then
    echo "✅ Trained model found"
else
    echo "⚠️  No trained model found"
    echo "   Please train the model using: notebooks/01_train_model.ipynb"
fi
echo ""

echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "📚 Next Steps:"
echo ""
echo "1. Train the model:"
echo "   jupyter notebook notebooks/01_train_model.ipynb"
echo ""
echo "2. Run the web app:"
echo "   python app/app.py"
echo ""
echo "3. Or use Google Colab:"
echo "   Open notebooks/complete_colab_workflow.ipynb in Colab"
echo ""
echo "🚀 Happy Learning!"
echo ""
