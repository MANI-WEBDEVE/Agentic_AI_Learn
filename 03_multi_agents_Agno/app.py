from agno.agent.agent import Agent
from agno.models.groq.groq import Groq
from agno.tools.googlesearch import GoogleSearch
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
if api_key:
    os.environ["GROQ_API_KEY"] = api_key
else:
    raise ValueError("GROQ_API_KEY is not set in the environment variables")


### web agent ###

web_agent=Agent(
    name="web Agent"
    ,model=Groq(id="deepseek-r1-distill-llama-70b")
    ,description="You are the web agent"
    ,tools=[GoogleSearch()]
    ,show_tool_calls=False
    ,markdown=True
)


#### finance agent ####

finance_agent=Agent(
    name="Finance Agent",
    role="Get Financial data",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    description="You are the finance agent",
    tools=[YFinanceTools(stock_price=True, company_info=True, analyst_recommendations=True)],
    instructions="Use table display data",
    show_tool_calls=False,
    markdown=True
    
)


def multi_agent():
    return Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    name="Team Agent",
    instructions=['always inclued source url and other source', "use table to display data", "and response Minglish language"],
    show_tool_calls=False,
    markdown=True
)



## team Agent
def multi_agent_response(query) -> str:
    response=multi_agent().run(query)
    response.content
    return response.content if response.content is not None else ""

