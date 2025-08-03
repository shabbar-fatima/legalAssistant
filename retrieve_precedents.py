from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# Load Chroma index
index = Chroma.load("legal_assistant_index")

# Initialize OpenAI model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Function to retrieve relevant precedents for a query
def get_relevant_precedents(query):
    # Use the index to find similar documents
    search_results = index.similarity_search(query, k=3)  # Top 3 relevant results
    
    # Combine the results into a string for context
    context = "\n".join([doc.page_content for doc in search_results])
    
    # Generate the answer using the context
    answer_chain = RetrievalQA.from_chain_type(llm=llm, retriever=index.as_retriever())
    response = answer_chain.run(query)
    
    return response

# Sample usage
query = "Can I claim my father's property as a daughter if my brother denies?"
precedent_response = get_relevant_precedents(query)
print("Precedent and Recommendation: ", precedent_response)
