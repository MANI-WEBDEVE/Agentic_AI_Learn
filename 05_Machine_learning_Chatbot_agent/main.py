import os
import streamlit as st
from dotenv import load_dotenv
from agno.agent.agent import Agent
from agno.models.groq.groq import Groq
from agno.embedder.google import GeminiEmbedder
from agno.vectordb.lancedb.lance_db import LanceDb
from agno.vectordb.search import SearchType
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.tools.googlesearch import GoogleSearch

# Page configuration
st.set_page_config(
    page_title="ML_Agent",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Initialize the session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

def agent_response(agent, query):
    """Get the response of Agent"""
    try:
        response = agent.run(query)
        return response.content
    except Exception as e:
        print(f"Error Found we {e}")
        return str(e)

def initialize_agent():
    """Initialize the Machine learning Agent"""
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    if api_key is None:
        raise ValueError("GOOGLE_GEMINI_API_KEY is not set in the environment variables.")
    else:
        print("lo")
        os.environ["GOOGLE_API_KEY"] = api_key

    deep_seek_api_key = os.getenv("GROQ_API_KEY")
    if deep_seek_api_key is None:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")
    else:
        print("lo2")
        os.environ["GROQ_API_KEY"] = deep_seek_api_key

    try:
        agent = Agent(
            model=Groq(id="deepseek-r1-distill-llama-70b"),
            description="You are the Machine learning Expert and Best Machine learning teacher",
            add_datetime_to_instructions=True,
            instructions=[
                "Search for knowledge base for Machine learning",
                "If the question is better suited for the web, search the web to fill in gaps.",
                "Prefer the information in your knowledge base over the web results."
            ],
            knowledge=PDFUrlKnowledgeBase(
                urls=["https://www.nrigroupindia.com/e-book/Introduction%20to%20Machine%20Learning%20with%20Python%20(%20PDFDrive.com%20)-min.pdf"],
                vector_db=LanceDb(
                    uri="temp/lancedb",
                    table_name="machine_learning_db",
                    search_type=SearchType.hybrid,
                    embedder=GeminiEmbedder()
                )
            ),
            tools=[GoogleSearch()],
            show_tool_calls=False,
            markdown=True
        )
        
        # Load knowledge base if not already loaded
        if agent.knowledge is not None and not hasattr(agent.knowledge, '_loaded'):
            agent.knowledge.load()
            # agent.knowledge.lo = True
            

        return agent
    except Exception as e:
        print(f"Error Found 23{e}")
        return None

def main():
    st.title("Machine Learning Chat bot")
    st.markdown("Ask me anything about Machine Learning related question")
    
    # Initialize agent
    if 'agent' not in st.session_state:
        with st.spinner("Initializing Machine learning expert..."):
            st.session_state.agent = initialize_agent()
    
    # Check if agent initialization was successful
    if st.session_state.agent is None:
        st.error("Failed to initialize the Machine learning expert. Please check your API keys and try again.")
        return
    
    # Display chat messages
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        with st.chat_message(role):
            st.markdown(content)
    
    # Chat input
    if prompt := st.chat_input("Ask about Machine learning..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Our Machine learning expert process..."):
                try:
                    response = agent_response(st.session_state.agent, prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_message = f"An error occurred: {str(e)}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})

if __name__ == "__main__":
    main()