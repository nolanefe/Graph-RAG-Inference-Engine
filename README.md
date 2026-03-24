# Graph-RAG-Inference-Engine

A knowledge graph-based RAG engine utilizing Neo4j and LangChain to eliminate LLM hallucinations through structured, deterministic querying.

### Core Architecture
* **Knowledge Graph Backend:** Uses Neo4j to store infrastructure relationships as nodes and edges, preventing the AI from guessing connections.
* **Deterministic Querying:** Implements LangChain's `GraphCypherQAChain` to translate human questions into strict Cypher database queries.
* **LLM Engine:** Powered by `gpt-4-turbo` for high-accuracy reasoning and natural language translation of database results.

### Tech Stack
* **Language:** Python 3.10+
* **Framework:** LangChain
* **Database:** Neo4j (Graph Database)
* **AI/LLM:** OpenAI (`gpt-4-turbo`)
* **Domain:** Retrieval-Augmented Generation (RAG), Knowledge Graphs

### Build and Execution
Note: Requires Python 3.10+, an OpenAI API Key, and Neo4j credentials.

 ```bash
1. Clone the repository
   git clone [https://github.com/nolanefe/Graph-RAG-Inference-Engine.git](https://github.com/nolanefe/Graph-RAG-Inference-Engine.git)
   cd Graph-RAG-Inference-Engine
   

2. Run and execute
   pip install -r requirements.txt
   python main.py
   ```
