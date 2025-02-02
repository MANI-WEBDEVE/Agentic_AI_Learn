import streamlit as st
from agent_with_tool import *
####### Page config ########
st.set_page_config(
    page_title="Hello",
    page_icon="🤖",
)

#### Page title ########

st.title("Movie Expliner Minglish language")
def new_func():
    return "Provide the name of the latest movie and the Agent will explain it."

st.markdown(new_func())

####### Intialize session  ########
if "agent" not in st.session_state:
    st.session_state.agent = createAgent()

##### input text area ########
query = st.text_area("Enter your prompt here", value="", height=100)

if st.button( label="Submit", type='primary'):
    with st.spinner("Generating News..."):
        try:
            response = get_Agent_response(st.session_state.agent, "Minglish language strickly and explain full movie"+query)
            st.markdown(response)
            st.toast("successfully!", icon="🎉")
        except Exception as e:
            st.error(f"An error occurred: {e}")



with st.sidebar:
    st.title("About")
    st.markdown(
        """
        This is a demo of the Agentic AI with deepseek R1 distill llama 70b and Agno.
        """
    )
    st.markdown("---")  # Horizontal line as separator
    st.title("Instructions")
    st.markdown(
        """
        1. Enter the name of the latest movie in the text area.
        2. Click on the 'Submit' button.
        3. Wait for the agent to generate the explanation.
        """
    )
    st.markdown("---")  # Horizontal line as separator
    st.title("Contact")
    st.markdown(
        """
        For any inquiries, please contact us at:
        <a href="https://m-inam.vercel.app/contact">Contact</a>
        """,
        unsafe_allow_html=True
    )
st.markdown("---")  # Horizontal line as separator
st.markdown(
    """
    <div style='text-align: center; color: grey; padding: 10px;'>
    Made with MANI-WEBDEVE | © 2025 All rights reserved
    </div>
    """, 
    unsafe_allow_html=True
)