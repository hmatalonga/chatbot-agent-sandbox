import streamlit as st

from litellm import completion

st.set_page_config(page_title="Chatbot Local Server", page_icon="🏺")

with st.sidebar:
    """
    For additional documentation, visit the following links:
    1. [Ollama](https://ollama.ai/)
    2. [LiteLLM](https://docs.litellm.ai/docs/)    
    """

st.title("🏺 Chatbot Local Server")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = completion(
        model="ollama/mistral:instruct",
        messages=st.session_state.messages,
        api_base="http://localhost:11434",
    )
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
