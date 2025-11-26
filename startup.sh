#!/bin/bash
set -x  # Enable debug output
exec 2>&1  # Redirect stderr to stdout so all output is captured

echo "Starting application..."
echo "Python version:"
python --version

echo "Current directory:"
pwd

echo "Listing files:"
ls -la

echo "Installing/verifying dependencies..."
pip install -r requirements.txt 2>&1 | tail -20

mkdir -p ~/.streamlit/
echo "[general]
email = \"\"
passwordsRequired = false
enableCORS = false

[server]
headless = true
enableXsrfProtection = false
port = ${PORT:-8000}
" > ~/.streamlit/config.toml

echo "Streamlit config created."
echo "Starting Streamlit..."
python -m streamlit run app.py --server.headless true
