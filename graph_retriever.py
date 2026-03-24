from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI
import os

graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"), 
    username=os.getenv("NEO4J_USER"), 
    password=os.getenv("NEO4J_PASSWORD")
)

llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

chain = GraphCypherQAChain.from_llm(
    llm=llm, 
    graph=graph, 
    verbose=True,
    return_intermediate_steps=True
)

def query_infrastructure(question: str):
    # Example: "What microservices rely on the Redis cache cluster?"
    response = chain.invoke({"query": question})
    return response['result']