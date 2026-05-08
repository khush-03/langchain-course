from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.agents import create
from tavily import TavilyClient
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field

load_dotenv()
# agent response object
class Source(BaseModel):
    """
    Schema for a source used by the agent
    """
    url:str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    """
    Schmea for agent response with answer and sources
    """
    answer:str = Field(description="the agents answer to the query")
    sources:List[Source] = Field(default_factory=list, description="list of sources used to generate the answers")
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
tools = [search] # or tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools,response_format=AgentResponse)

result= agent.invoke({"messages":HumanMessage(content="whats the weather in tokyo")})

print(result)