import streamlit as st
import os
import tempfile
from rag_engine import RAGEngine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="DocuChat RAG", page_icon="📚")

st.title("📚 DocuChat: Chat with your Documents")
st.markdown("""
This app demonstrates **Vectorization** and **Indexing**. 
Upload your documents (PDF or TXT) to create a knowledge base and ask questions!
""")

# Sidebar for configuration and file upload
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    
    st.header("Knowledge Base")
    uploaded_files = st.file_uploader("Upload Documents", type=["pdf", "txt"], accept_multiple_files=True)
    
    st.header("Custom Prompt")
    default_prompt = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer concise.

Context: {context}

Question: {question}

Helpful Answer:"""
    custom_prompt = st.text_area("Define your prompt:", value=default_prompt, height=200)
    
    process_btn = st.button("Process Documents")

# Initialize session state
if "rag_engine" not in st.session_state:
    st.session_state.rag_engine = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Processing Logic
if process_btn and uploaded_files and api_key:
    with st.spinner("Processing documents... This involves splitting text, vectorizing it, and building the index."):
        try:
            # Save uploaded files to temp dir to be read by loaders
            temp_dir = tempfile.mkdtemp()
            file_paths = []
            for uploaded_file in uploaded_files:
                path = os.path.join(temp_dir, uploaded_file.name)
                with open(path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                file_paths.append(path)
            
            # Initialize Engine
            st.session_state.rag_engine = RAGEngine(api_key)
            
            status = st.session_state.rag_engine.ingest_documents(file_paths, custom_prompt)
            st.success(status)
            
            # Show the prompt being used
            with st.expander("View Active System Prompt"):
                st.text(st.session_state.rag_engine.get_current_prompt())
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
elif process_btn and not api_key:
    st.warning("Please enter your OpenAI API Key.")

# Chat Interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about your documents..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    if st.session_state.rag_engine:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.rag_engine.get_response(prompt)
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.warning("Please upload and process documents first.")
