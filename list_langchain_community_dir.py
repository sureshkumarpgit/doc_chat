import os
import langchain_community

path = langchain_community.__path__[0]
print(f"Listing contents of: {path}")
try:
    print(os.listdir(path))
except Exception as e:
    print(e)
