FROM python:3.13.8-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY streamlit_app.py .
COPY rag_engine.py .
COPY .streamlit/ .streamlit/

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8000/_stcore/health || exit 1

# Run Streamlit
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8000", "--server.address=0.0.0.0", "--server.headless=true", "--logger.level=warning"]
