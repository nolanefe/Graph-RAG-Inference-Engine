from graph_retriever import query_infrastructure

if __name__ == "__main__":
    print("Initializing Graph-RAG Inference Engine...\n")
    
    # Example query to test the system
    question = "What microservices rely on the Redis cache cluster?"
    print(f"Querying: {question}\n")
    
    try:
        answer = query_infrastructure(question)
        print("Result:")
        print(answer)
    except Exception as e:
        print(f"Error during graph retrieval: {e}")