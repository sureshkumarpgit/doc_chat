"""
Azure App Service Streamlit wrapper.
Runs Streamlit with proper Azure compatibility.
"""
import os
import sys

# Set port before any imports
port = os.environ.get("PORT", "8000")
os.environ["STREAMLIT_SERVER_PORT"] = port
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_CLIENT_TOOLBAR_MODE"] = "minimal"

print(f"[INIT] Port: {port}", file=sys.stderr, flush=True)
print(f"[INIT] Python: {sys.version}", file=sys.stderr, flush=True)
print(f"[INIT] CWD: {os.getcwd()}", file=sys.stderr, flush=True)

try:
    # Import streamlit - this will fail if there's an issue
    import streamlit.cli as cli
    print("[INIT] Streamlit imported successfully", file=sys.stderr, flush=True)
    
    # Run streamlit
    sys.argv = ["streamlit", "run", "app.py", "--logger.level=info"]
    print(f"[INIT] Starting with args: {sys.argv}", file=sys.stderr, flush=True)
    sys.exit(cli.main())
    
except ImportError as e:
    print(f"[ERROR] Import error: {e}", file=sys.stderr, flush=True)
    sys.exit(1)
except Exception as e:
    print(f"[ERROR] {type(e).__name__}: {e}", file=sys.stderr, flush=True)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)
