"""
Flask WSGI app that proxies to Streamlit.
This allows Azure to detect and run the app properly.
"""
import subprocess
import sys
import os
import atexit
from threading import Thread

# Start Streamlit in a background thread
def start_streamlit():
    port = os.environ.get('PORT', '8000')
    os.environ['STREAMLIT_SERVER_PORT'] = str(int(port) + 1)  # Run on PORT+1
    os.environ['STREAMLIT_SERVER_ADDRESS'] = '127.0.0.1'  # Only localhost
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    
    cmd = [
        sys.executable,
        '-m',
        'streamlit',
        'run',
        'app_streamlit.py',
        '--logger.level=warning'
    ]
    
    print(f"[WSGI] Starting Streamlit on port {os.environ['STREAMLIT_SERVER_PORT']}")
    subprocess.Popen(cmd)

# Start Streamlit on import
streamlit_thread = Thread(target=start_streamlit, daemon=True)
streamlit_thread.start()

# Dummy Flask app (for Azure detection)
def app(environ, start_response):
    """WSGI application - redirects to Streamlit."""
    path = environ.get('PATH_INFO', '/')
    
    # Simple health check response
    if path == '/health':
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [b'OK']
    
    # Default response (Streamlit will handle via reverse proxy)
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'<meta http-equiv="refresh" content="0; url=/app" />']
