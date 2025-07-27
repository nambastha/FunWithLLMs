import streamlit as st
import requests

OLLAMA_API = "http://<NODE-IP>:11434/api/generate"

st.set_page_config(page_title="💬OllamaChat", layout="centered")
st.markdown("<h1 style='text-align: center;'>💬OllamaChat</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose a model and ask anything!</p>", unsafe_allow_html=True)
st.divider()

model = st.selectbox("Choose a model", ["phi3", "mistral", "llama3"])
st.markdown(f"<p style='text-align: left;'>Using model: <code>{model}</code></p>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display full history except the latest prompt being processed
for role, msg in st.session_state.chat_history:
    with st.chat_message(role, avatar="👤" if role == "user" else "🧠"):
        st.markdown(msg)

# Input box
user_prompt = st.chat_input("Type your message...")

# Handle input
if user_prompt:
    # Show user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_prompt)

    # Append user message to history
    st.session_state.chat_history.append(("user", user_prompt))

    # Get assistant response and display once
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Thinking..."):
            try:
                res = requests.post(OLLAMA_API, json={
                    "model": model,
                    "prompt": user_prompt,
                    "stream": False
                }, timeout=60)
                res.raise_for_status()
                reply = res.json().get("response", "🤖 No response received.")
            except Exception as e:
                reply = f"⚠️ Error: {e}"

            st.markdown(reply)
            st.session_state.chat_history.append(("assistant", reply))
