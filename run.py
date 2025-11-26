#!/usr/bin/env python
"""
Simple wrapper to run Streamlit on Azure App Service.
This approach bypasses web.config limitations.
"""
import os
import sys
import subprocess

if __name__ == "__main__":
    # Get port from environment or default to 8000
    port = os.environ.get('PORT', '8000')
    
    # Log startup
    print(f"[STARTUP] Starting Streamlit application on port {port}")
    print(f"[STARTUP] Python: {sys.executable}")
    print(f"[STARTUP] Version: {sys.version}")
    sys.stdout.flush()
    
    # Set required environment variables
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    os.environ['STREAMLIT_SERVER_PORT'] = port
    os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
    os.environ['STREAMLIT_LOGGER_LEVEL'] = 'debug'
    
    try:
        # Run streamlit directly
        subprocess.call([
            sys.executable, 
            '-m', 
            'streamlit',
            'run',
            'app.py',
            '--logger.level=debug',
            f'--server.port={port}',
            '--server.address=0.0.0.0',
            '--server.headless=true'
        ])
    except Exception as e:
        print(f"[ERROR] Failed to start Streamlit: {e}", file=sys.stderr)
        sys.exit(1)
