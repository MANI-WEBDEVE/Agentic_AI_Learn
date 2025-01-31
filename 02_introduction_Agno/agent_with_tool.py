from agno.agent import Agent
from agno.models.groq import Groq 
import os
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
load_dotenv()

# os.environ["GROQ_DEEPSEEK_API"] = os.getenv("GROQ_DEEPSEEK_API")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b" ),
    description="your a agent for Muhammad Inam and Muhammad Inam not understand the English language that is use Minglisg language strickly okay",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

agent.print_response(" ", stream=True)
