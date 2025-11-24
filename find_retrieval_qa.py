import pkgutil
import langchain

print(f"LangChain path: {langchain.__path__}")

try:
    from langchain.chains import RetrievalQA
    print("SUCCESS: Found RetrievalQA in langchain.chains")
except ImportError as e:
    print(f"FAILURE: langchain.chains - {e}")

try:
    from langchain_community.chains import RetrievalQA
    print("SUCCESS: Found RetrievalQA in langchain_community.chains")
except ImportError as e:
    print(f"FAILURE: langchain_community.chains - {e}")

try:
    from langchain.chains.retrieval_qa.base import RetrievalQA
    print("SUCCESS: Found RetrievalQA in langchain.chains.retrieval_qa.base")
except ImportError as e:
    print(f"FAILURE: langchain.chains.retrieval_qa.base - {e}")
