from langchain.prompts import PromptTemplate

template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer concise.

Context: {context}

Question: {question}

Helpful Answer:"""

try:
    prompt = PromptTemplate.from_template(template)
    print(f"Input Variables: {prompt.input_variables}")
    
    if "context" not in prompt.input_variables:
        print("ERROR: 'context' missing from input_variables")
    else:
        print("SUCCESS: 'context' found.")
        
except Exception as e:
    print(f"Exception: {e}")
