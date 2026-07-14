import streamlit as st
import google.generativeai as genai


API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# Page Config
st.set_page_config(
    page_title="AI Multiverse",
    layout="wide"
)

st.title("🌌 AI Multiverse")

st.write("Talk with different AI personalities powered by Gemini!")

# TASK 1
# Sidebar

st.sidebar.title("App Settings")

# TASK 2
# Persona Expansion

personality = st.sidebar.selectbox(

    "Choose a Personality",

    [

        "Helpful Assistant ",

        "Panicked College Student ",

        "1920s Mafia Boss ",

        "Sarcastic Fitness Coach ",

        "Shakespeare ",

        "Pirate Captain ",


    ]

)

# TASK 3
# Intensity Slider

intensity = st.sidebar.slider(

    "Intensity Level",

    min_value=1,

    max_value=10,

    value=5

)

# User Input

user_input = st.text_input(" Ask Anything")

# TASK 5
# Dynamic Avatar

if personality == "Helpful Assistant ":
    bot_avatar = "🤖"

elif personality == "Panicked College Student 😰":
    bot_avatar = "😰"

elif personality == "1920s Mafia Boss 🕴️":
    bot_avatar = "🕴️"

elif personality == "Sarcastic Fitness Coach 💪":
    bot_avatar = "💪"

elif personality == "Shakespeare 🎭":
    bot_avatar = "🎭"

elif personality == "Pirate Captain 🏴‍☠️":
    bot_avatar = "🏴‍☠️"

else:
    bot_avatar = "🤖"

# SEND BUTTON

if st.button("SEND"):

    if user_input.strip() == "":
        st.warning("Please enter a message.")

    else:

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

Respond to the user's message naturally.

User:
{user_input}
"""

        response = model.generate_content(ai_instructions)

        # TASK 4
        # Chat UI

        with st.chat_message("user", avatar="🙂"):

            st.write(user_input)

        with st.chat_message("assistant", avatar=bot_avatar):

            st.write(response.text)