# 🇵🇰 Legal-AI Assistant for Pakistan  
**Document Summarization, Precedent Retrieval & Decision Suggestion using RAG**

This repository contains the code and data for a legal assistant system designed specifically for the Pakistani legal domain. It leverages Retrieval-Augmented Generation (RAG) to assist in legal research, case summarization, and AI-guided recommendations — helping lawyers, students, and analysts work more efficiently with local case law.

---

## Features

-  **Legal Document Summarization**  
  Extracts and condenses lengthy case files into readable summaries, highlighting key facts, decisions, and legal issues.

-  **Precedent Retrieval**  
  Uses embedding-based semantic search (e.g., `text-embedding-ada-002` + FAISS/ChromaDB) to find relevant Pakistani precedents based on a case description or query.

-  **Decision Suggestion**  
  Generates legally grounded suggestions and interpretations using an LLM (e.g., GPT-4 or open-source alternatives), conditioned on retrieved case law.

- 🇵🇰 **Local Language Support**  
  Capable of understanding and responding in both **English** and **Urdu**, trained on region-specific legal terminology and hybrid formal/informal phrasing.
 
## Prerequisites

This README provides step-by-step instructions to set up a Python environment with necessary libraries, install and configure Redis using Docker, and run a Streamlit application that integrates Redis for memory management.
- Python 3.7 or later
- Docker Desktop
 
## Steps
 
### 1. Install Python Libraries
Install the required Python libraries using pip:
```sh
pip install streamlit langchain_google_genai
```
 
### 2. Install Docker Desktop
Download and install Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop).
 
### 3. Pull Redis Image
Open a terminal or command prompt and run the following command to download the Redis image for Docker:
```sh
docker pull redis/redis-stack:latest
```
 
### 4. Install Redis Client for Python
Run the following command to install the Redis client library for Python:
```sh
pip install --upgrade --quiet redis
```
 
### 5. Run Redis Container
Start a Redis container using Docker with the following command:
```sh
docker run -d -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```
 
### 6. Generate embadding DB
Navigate to the directory containing generate_embeddings.py and run the following command:
``` sh
python generate_embeddings.py
```
note: Embedding db is already generated and is part of current project. however if you want to create db again make sure to delete the previous files and add the required PDFs in the data folder before executing the command

### 7. Run Streamlit Application
Navigate to the directory containing your Streamlit application script (`app_with_redis_memory.py`) and run the following command:
```sh
streamlit run app_with_redis_memory.py
```
 
## Additional Notes
- Ensure Docker Desktop is running before executing the Docker commands.
- The Redis container will be accessible on port 6379, and the RedisInsight GUI will be available on port 8001.
- If you encounter any issues, check the Docker and Streamlit documentation for troubleshooting tips.
 
## Conclusion
Following these steps, you should have a working environment with Python, Streamlit, and Redis integrated. This setup will allow you to run applications that utilize Redis for memory management efficiently.





