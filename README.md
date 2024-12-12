# AI Trademark Recommendation System

## Introduction
The **AI Trademark Recommendation System** is designed to simplify the process of searching for trademarks. By leveraging advanced AI techniques and a vector database, this system ensures that users receive accurate and relevant trademark recommendations based on their queries.

## Description
This project is built to provide users with the top trademark recommendations from the United States Patent and Trademark Office (USPTO) database. It combines the power of **Pinecone vector database** for efficient data retrieval and **Cohere's Rerank model** for refining the search results. The final output, consisting of the top 5 trademark descriptions, is delivered to users through an intuitive **Streamlit-based frontend**.

### Key Features:
- **Vector Search:** Uses Pinecone for storing and retrieving trademark data efficiently.
- **Hybrid Search:** Combines vector-based and traditional search methods to retrieve the top 25 relevant trademarks.
- **Reranking:** Utilizes Cohere's Rerank model to refine the results and present the top 5 most relevant trademarks.
- **User-Friendly Interface:** The recommendations are displayed on a simple, interactive Streamlit application.

## Tools and Technologies
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Vector Database:** Pinecone
- Langchain
- **AI Models:**
  - Hybrid search for initial data retrieval
  - Cohere's Rerank model for result refinement
- **Data Source:** USPTO Trademark Database

## How It Works
1. **Data Storage in Pinecone:**
   - All trademark data from the USPTO is preprocessed and stored in Pinecone as vector embeddings.

2. **Query Submission:**
   - The user inputs a trademark-related query via the Streamlit app frontend.

3. **Hybrid Search:**
   - The query is sent to the Pinecone vector database.
   - A hybrid search retrieves the top 25 relevant trademarks based on the query.

4. **Reranking with Cohere:**
   - The retrieved results are sent to Cohere's Rerank model.
   - The model processes the data and returns the top 5 most relevant trademarks.

5. **Displaying Results:**
   - The top 5 trademark descriptions are displayed on the Streamlit application for the user in form of table.

---

Feel free to contribute or raise any issues in this repository to improve the functionality of the system. 😊
