try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    print("SUCCESS: langchain_text_splitters imported successfully.")
except ImportError as e:
    print(f"FAILURE: {e}")

try:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    print("SUCCESS: langchain.text_splitter imported successfully.")
except ImportError as e:
    print(f"FAILURE: {e}")
