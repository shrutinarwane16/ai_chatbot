import streamlit as st
from chatbot import get_chat_response

st.set_page_config(page_title="AI Chatbot")

st.title("🤖 My AI Chatbot")

# Save chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Temperature slider
temperature = st.sidebar.slider(
    "Creativity Level",
    0.0, 1.0, 0.7
)

# Clear chat button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    st.rerun()

# Show previous messages
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box
if prompt := st.chat_input("Type your message..."):

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # Show assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_chat_response(
                st.session_state.messages,
                temperature
            )
            st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )