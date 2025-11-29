from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("realistic_restaurant_reviews.csv")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids= []

    for i,row in df.iterrows():
        document =Document(
            page_content = row["Title"]+" "+row["Review"]
            metadata={"rating":row["rating"],"date":row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
    
