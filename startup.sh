#!/bin/bash
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"\"\n\
passwordsRequired = false\n\
enableCORS = false\n\
\n\
[server]\n\
headless = true\n\
enableXsrfProtection = false\n\
port = ${PORT:-8000}\n\
" > ~/.streamlit/config.toml
python -m streamlit run app.py --server.headless true
