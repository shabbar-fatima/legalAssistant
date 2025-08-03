import os
import chromadb
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# Initialize ChromaDB client
client = chromadb.Client()

# Specify the folder containing legal documents
document_folders = ['contracts', 'court judgements', 'laws of pakistan']

# Function to load and index documents
def index_documents():
    # Load documents from folders
    documents = []
    for folder in document_folders:
        folder_path = os.path.join(os.getcwd(), folder)
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    documents.append(content)
    
    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings()

    # Create and store documents in Chroma
    docsearch = Chroma.from_documents(documents, embeddings)
    
    # Saving the index for later use
    docsearch.persist("legal_assistant_index")

# Run the index function to index all documents
index_documents()
