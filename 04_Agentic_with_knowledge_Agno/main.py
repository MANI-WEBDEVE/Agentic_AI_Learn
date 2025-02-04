from agno.agent.agent import Agent
from agno.models.google.gemini import Gemini
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb.lance_db import LanceDb
from agno.models.groq.groq import Groq
from agno.embedder.google import GeminiEmbedder
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
if api_key is None:
    raise ValueError("GOOGLE_GEMINI_API_KEY is not set in the environment variables.")
else:
    os.environ["GOOGLE_API_KEY"] = api_key

deep_seek_api_key = os.getenv("GROQ_API_KEY")

if deep_seek_api_key is None:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")
else:
    os.environ["GROQ_API_KEY"] = deep_seek_api_key

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://www.nrigroupindia.com/e-book/Introduction%20to%20Machine%20Learning%20with%20Python%20(%20PDFDrive.com%20)-min.pdf"],
    vector_db=LanceDb(
        table_name="machine_learning_guide",
        uri="temp/lancedb",
        embedder=GeminiEmbedder()
    ),
    
)

# knowledge_base.load(recreate=True)


agent=Agent(
    # model=Gemini(id="gemini-2.0-flash-exp"),
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    knowledge=knowledge_base,
    show_tool_calls=True
)



agent.print_response('Why sky blue', stream=True)