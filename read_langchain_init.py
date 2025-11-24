import langchain
print(f"File: {langchain.__file__}")
with open(langchain.__file__, 'r') as f:
    print(f.read())
