from agno.agent import Agent
from agno.models.groq import Groq 
import os
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.googlesearch import GoogleSearch
load_dotenv()
# 
# os.environ["GROQ_DEEPSEEK_API"] = os.getenv("GROQ_DEEPSEEK_API")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

def createAgent():
    return Agent(
        model=Groq(id="deepseek-r1-distill-llama-70b"),
        description="You are the movie explainer in Minglish language",
        tools=[GoogleSearch()],
        show_tool_calls=False,
        parse_response=True,
        structured_outputs=True,
        markdown=True
    )

def get_Agent_response(agent, query):
    try:
        response = agent.run(query)
        return response.content
    except Exception as e:
        return f"An error occurred: {e}"    