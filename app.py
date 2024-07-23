from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
import gc 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

## Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo", layout="wide")
st.header("Let's Talk here")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

MAX_HISTORY_LENGTH = 20  

if submit and input:
    with st.spinner('Waiting for the response...'):
        response = get_gemini_response(input)
        # Concatenate all response chunks into one string
        full_response = ''.join([chunk.text for chunk in response])
        
    # Add user query and full concatenated response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.session_state['chat_history'].append(("Bot", full_response))

    # Ensure chat history does not exceed maximum length
    if len(st.session_state['chat_history']) > MAX_HISTORY_LENGTH:
        st.session_state['chat_history'] = st.session_state['chat_history'][-MAX_HISTORY_LENGTH:]

    # Explicitly call garbage collection
    gc.collect()

# Custom CSS to style the chat messages
st.markdown(
    """
    <style>
    .chatbox {
        border: 1px solid #ccc;
        border-radius: 25px;
        padding: 10px;
        margin: 10px 0;
    }
    .user {
        color: white;
        background-color: #025246;
        text-align: left;
    }
    .bot {
        color: white;
        background-color: #016969;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display chat history
st.subheader("Chat History:")
for role, text in st.session_state['chat_history']:
    align_class = "user" if role == "You" else "bot"
    st.markdown(f'<div class="chatbox {align_class}">{text}</div>', unsafe_allow_html=True)
