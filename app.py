import streamlit as st
import google.generativeai as genai

# Gemini Configuration

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# Assignment 3
# Memory Vault

if "messages" not in st.session_state:
    st.session_state.messages = []

# Page Config

st.set_page_config(
    page_title="AI Multiverse",
    layout="wide"
)

st.title("🌌 AI Multiverse")
st.write("Talk with different AI personalities powered by Gemini!")

# Sidebar

st.sidebar.title("⚙️ App Settings")

personality = st.sidebar.selectbox(
    "Choose a Personality",
    [
        "Helpful Assistant 🤖",
        "Panicked College Student 😰",
        "1920s Mafia Boss 🕴️",
        "Sarcastic Fitness Coach 💪",
        "Shakespeare 🎭",
        "Pirate Captain 🏴‍☠️"
    ]
)

intensity = st.sidebar.slider(
    "Intensity Level",
    min_value=1,
    max_value=10,
    value=5
)

# Dynamic Avatar

avatar_map = {
    "Helpful Assistant 🤖": "🤖",
    "Panicked College Student 😰": "😰",
    "1920s Mafia Boss 🕴️": "🕴️",
    "Sarcastic Fitness Coach 💪": "💪",
    "Shakespeare 🎭": "🎭",
    "Pirate Captain 🏴‍☠️": "🏴‍☠️"
}

bot_avatar = avatar_map.get(personality, "🤖")

# Display Previous Chat History

for message in st.session_state.messages:

    avatar = "🙂" if message["role"] == "user" else bot_avatar

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Chat Input (Assignment 3)

if user_input := st.chat_input("Say something..."):

    # Display User Message

    with st.chat_message("user", avatar="🙂"):
        st.markdown(user_input)

    # Save User Message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Conversation History

    history = ""

    for msg in st.session_state.messages:
        history += f"{msg['role']}: {msg['content']}\n"

    # Prompt Engineering

    ai_instructions = f"""
You are acting as:

{personality}

Intensity Level:

{intensity}/10

If the intensity is low,
behave only slightly like the personality.

If the intensity is high,
fully immerse yourself in the character while still answering accurately.

Continue the conversation naturally using the previous conversation history.

Conversation History:

{history}

User:
{user_input}
"""

    # Gemini Response

    response = model.generate_content(ai_instructions)

    # Display Assistant Response

    with st.chat_message("assistant", avatar=bot_avatar):
        st.markdown(response.text)

    # Save Assistant Response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )