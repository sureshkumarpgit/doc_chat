# DocuChat: GPT-based RAG Chatbot

This is a Python application that allows you to chat with your documents using OpenAI's GPT models. It demonstrates the concepts of **Vectorization** (embedding text into numbers) and **Indexing** (storing vectors for fast retrieval).

## Features
-   **Document Ingestion**: Upload PDF or TXT files.
-   **RAG Pipeline**: Uses LangChain to split text, create embeddings, and index them using FAISS.
-   **Chat Interface**: A Streamlit web app to query your knowledge base.

## Setup

1.  **Clone the repository** (or navigate to the project directory).

2.  **Create a Virtual Environment** (recommended):
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables**:
    -   Rename `.env.example` to `.env`.
    -   Add your OpenAI API Key to `.env`:
        ```
        OPENAI_API_KEY=sk-...
        ```

## Running the App

Run the Streamlit application:
```bash
streamlit run app.py
```

## How it Works
1.  **Vectorization**: When you upload a document, it is split into chunks. Each chunk is converted into a vector (a list of numbers) using OpenAI's embedding model.
2.  **Indexing**: These vectors are stored in a FAISS index, which allows for extremely fast similarity search.
3.  **Retrieval**: When you ask a question, your query is also converted into a vector. The system finds the most similar chunks in the index.
4.  **Generation**: The relevant chunks are sent to GPT-4 along with your question to generate an accurate answer.
