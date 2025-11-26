#!/bin/bash
set -e

echo "[STARTUP] Starting DocuChat application..."
echo "[STARTUP] Current directory: $(pwd)"
echo "[STARTUP] Python version:"
python --version
echo "[STARTUP] Python path: $(which python)"

# Create .streamlit directory if needed
mkdir -p ~/.streamlit/

# Export environment variables
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_SERVER_PORT=${PORT:-8000}
export STREAMLIT_SERVER_ADDRESS=0.0.0.0

echo "[STARTUP] PORT: $STREAMLIT_SERVER_PORT"
echo "[STARTUP] Starting Streamlit..."

# Run the Python wrapper
python run.py
