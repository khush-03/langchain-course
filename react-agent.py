from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.agents import create
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

#for normal python function to tool 
@tool
def search(query: str)-> str:
    """
    Tool that searches over the internet
    Args:
        query: The query to search or 
    Returns:
        The search result
    """

    print("searching for {query}")
    #return "weather in tokyo is sunny"
    return tavily.search(query=query)

#llm = ChatOpenAI()
llm = ChatOllama()
tools = [search]. # or tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

result= agent.invoke({"messages":HumanMessage(content="whats the weather in tokyo")})

print(result)