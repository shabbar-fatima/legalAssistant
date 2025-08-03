from langchain.chains.summarize import summarize
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma

# Load Chroma index
index = Chroma.load("legal_assistant_index")

# Function to generate summary of a document
def summarize_document(document_text):
    prompt = f"Summarize this legal document: {document_text}"

    # Initialize OpenAI GPT model for summarization
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Summarizing using OpenAI GPT-3
    response = llm.run(prompt)
    return response

# Sample usage
document_text = "The contract states that..."
summary = summarize_document(document_text)
print("Summary: ", summary)
