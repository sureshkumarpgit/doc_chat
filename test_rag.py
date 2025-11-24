import os
from rag_engine import RAGEngine

def test_rag_pipeline():
    print("Testing RAG Pipeline...")
    
    # Check for API Key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your environment or .env file to run this test.")
        return

    # Create a dummy file for testing
    test_file = "test_doc.txt"
    with open(test_file, "w") as f:
        f.write("Antigravity is a powerful AI coding assistant developed by Google Deepmind. It helps users write code efficiently.")
    
    try:
        # Initialize Engine
        engine = RAGEngine(api_key)
        
        # Ingest
        print("Ingesting document...")
        status = engine.ingest_documents([test_file])
        print(status)
        
        # Query
        query = "Who developed Antigravity?"
        print(f"Querying: {query}")
        response = engine.get_response(query)
        print(f"Response: {response}")
        
        if "Deepmind" in response or "Google" in response:
            print("SUCCESS: Retrieved correct information.")
        else:
            print("FAILURE: Did not retrieve correct information.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cleanup
        if os.path.exists(test_file):
            os.remove(test_file)

if __name__ == "__main__":
    test_rag_pipeline()
