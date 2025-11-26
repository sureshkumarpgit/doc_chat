#!/bin/bash
export STREAMLIT_SERVER_PORT=${PORT:-8000}
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true

python -m streamlit run app.py --logger.level=warning
