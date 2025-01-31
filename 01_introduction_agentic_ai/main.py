from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv
import os
import asyncio
 
load_dotenv() 

api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

async def agent_ai():
   agent= Agent(
        task="search Muhammad Inam MANI-WEBDEVE and open github copy the bio with followers",
        llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)
    )
   result = await agent.run()
   print(result)

asyncio.run(agent_ai())