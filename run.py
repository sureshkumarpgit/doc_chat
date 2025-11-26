import subprocess
import os
import sys

if __name__ == "__main__":
    # Run Streamlit directly
    port = os.environ.get('PORT', '8000')
    
    cmd = [
        sys.executable,
        '-m',
        'streamlit',
        'run',
        'app.py',
        '--server.port', port,
        '--server.address', '0.0.0.0',
        '--server.headless', 'true',
    ]
    
    print(f"Starting Streamlit with command: {' '.join(cmd)}")
    subprocess.run(cmd)
