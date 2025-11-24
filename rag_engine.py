import os
from typing import List, Dict, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, AzureChatOpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate

class RAGEngine:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.vector_store = None
        self.chain = None
        
        # Initialize Embeddings based on provider
        if self.config['provider'] == 'Azure OpenAI':
            self.embeddings = AzureOpenAIEmbeddings(
                azure_deployment=self.config['azure_embedding_deployment'],
                openai_api_version=self.config['azure_api_version'],
                azure_endpoint=self.config['azure_endpoint'],
                api_key=self.config['api_key']
            )
        else:
            os.environ["OPENAI_API_KEY"] = self.config['api_key']
            self.embeddings = OpenAIEmbeddings()

    def ingest_documents(self, file_paths: List[str], custom_prompt: str = None):
        """
        Loads documents, splits them, and creates a vector index.
        """
        documents = []
        for file_path in file_paths:
            if file_path.endswith(".pdf"):
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())
            elif file_path.endswith(".txt"):
                loader = TextLoader(file_path)
                documents.extend(loader.load())
        
        if not documents:
            return "No documents loaded."

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)

        # Vectorization and Indexing
        self.vector_store = FAISS.from_documents(chunks, self.embeddings)
        
        # Initialize LLM based on provider
        if self.config['provider'] == 'Azure OpenAI':
            llm = AzureChatOpenAI(
                azure_deployment=self.config['azure_llm_deployment'],
                openai_api_version=self.config['azure_api_version'],
                azure_endpoint=self.config['azure_endpoint'],
                api_key=self.config['api_key'],
                temperature=0
            )
        else:
            llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
        
        # Define prompt
        if custom_prompt:
            template = custom_prompt
            # Auto-append placeholders if missing
            if "{context}" not in template:
                template += "\n\nContext: {context}"
            if "{question}" not in template:
                template += "\n\nQuestion: {question}"
        else:
            template = """Use the following pieces of context to answer the question at the end. 
            If you don't know the answer, just say that you don't know, don't try to make up an answer. 
            Use three sentences maximum and keep the answer concise.
            
            Context: {context}
            
            Question: {question}
            
            Helpful Answer:"""
        
        QA_CHAIN_PROMPT = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )

        self.chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(),
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
        )
        
        return f"Successfully processed {len(documents)} documents and created {len(chunks)} chunks."

    def get_response(self, query: str) -> str:
        """
        Retrieves relevant context and generates a response.
        """
        if not self.chain:
            return "Please upload and process documents first."
        
        response = self.chain.invoke(query)
        return response['result']

    def get_current_prompt(self) -> str:
        """
        Returns the current prompt template being used.
        """
        if self.chain:
            # Accessing the prompt from the chain structure
            return self.chain.combine_documents_chain.llm_chain.prompt.template
        return "No prompt loaded."
