#!/bin/bash
set -x
exec 2>&1

echo "Starting Streamlit application..."
python --version

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

python -m streamlit run app.py --server.headless true
