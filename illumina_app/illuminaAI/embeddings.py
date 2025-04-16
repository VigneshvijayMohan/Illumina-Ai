from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import os



def embed(docs, dbname):
    embedding = OpenAIEmbeddings(
        model="text-embedding-3-large",
        openai_api_key="your-openai-key"
    )

    #VectorDB
    persist_directory = f'docs/{dbname}/'


    # rm -rf docs/chroma/


    if not os.path.exists(persist_directory):
        # If the folder doesn't exist, create a new DB and add documents
        vectordb = Chroma.from_documents(
            documents=docs,
            embedding=embedding,
            persist_directory=persist_directory
        )
    else:
        # Load existing DB
        vectordb = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding
        )
    return vectordb

