from agno.agent import Agent
from agno.models.groq import Groq 
import os
from dotenv import load_dotenv

load_dotenv()

# os.environ["GROQ_DEEPSEEK_API"] = os.getenv("GROQ_DEEPSEEK_API")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b" ),
    description="your a agent for Muhammad Inam and Muhammad Inam not understand the English language that is use Minglisg language strickly okay",
    markdown=True
)

agent.print_response("Ma Muhammad Inam or mujha indonasian Horror movie buhat passan hai tum mujha ak new movie explain karo with story in Minglish language", stream=True)
