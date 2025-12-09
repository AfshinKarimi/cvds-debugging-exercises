#!/bin/bash
# Simple script to run all exercises
# Assumes setup has been completed

set -e

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run all exercises
python3 run_all_exercises.py

