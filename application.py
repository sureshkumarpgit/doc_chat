"""
Default application entry point for Azure.
Redirects to Streamlit.
"""
import os
import subprocess
import sys
from threading import Thread

def start_streamlit():
    """Start Streamlit in background"""
    port = os.environ.get('PORT', '8000')
    cmd = [
        sys.executable,
        '-m',
        'streamlit',
        'run',
        'streamlit_app.py',
        '--server.port', port,
        '--server.address', '0.0.0.0',
        '--server.headless', 'true',
        '--logger.level', 'warning'
    ]
    subprocess.run(cmd)

# Start Streamlit
streamlit_thread = Thread(target=start_streamlit, daemon=False)
streamlit_thread.start()
streamlit_thread.join()
