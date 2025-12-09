#!/bin/bash
# Setup script for cvds-debugging-exercises
# This script automates the setup process for reviewers

set -e  # Exit on error

echo "=========================================="
echo "Setting up cvds-debugging-exercises"
echo "=========================================="

# Check Python version
echo "Checking Python version..."
python3 --version || { echo "Error: Python 3 is required but not found"; exit 1; }

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "To run all exercises, use:"
echo "  source venv/bin/activate"
echo "  python3 run_all_exercises.py"
echo ""
echo "Or simply run:"
echo "  ./run.sh"
echo ""

