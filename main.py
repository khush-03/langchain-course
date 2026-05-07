from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import os

load_dotenv()
def main():
    print("Hello from langchain-course!")

    information="""
   hi i am khush jay brahmbhatt
    """
    summary_template="""
    given the information {information} about a person i want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model="gpt-5") # calling through paid API
    
    # using open source models like ollama
    # temperature defines creativity more temp more creative/abstract the response
    llm = ChatOllama(temperature=0, model = "gemma3:1b")

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)
if __name__ == "__main__":
    main()
