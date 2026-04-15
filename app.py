import streamlit as st
import os
import pandas as pd
from dotenv import load_dotenv

from pdf_handler import extract_text_from_pdfs
from vector_store import create_vector_store
from chatbot import get_response
st.markdown("""
<style>
.chat-container {
    display: flex;
    flex-direction: column;
}

.user-message {
    background-color: #DCF8C6;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    align-self: flex-end;
    max-width: 70%;
}

.bot-message {
    background-color: #F1F0F0;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    align-self: flex-start;
    max-width: 70%;
}
</style>
""", unsafe_allow_html=True)
load_dotenv()

st.title("📄 RAG PDF Analyser")

# Sidebar
api_key = st.sidebar.text_input("Enter API Key", type="password")

pdf_files = st.sidebar.file_uploader(
    "Upload PDFs",
    accept_multiple_files=True
)

if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key

# Memory
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chat" not in st.session_state:
    st.session_state.chat = []

# Process PDFs
if st.sidebar.button("Process"):
    if pdf_files:
        text = extract_text_from_pdfs(pdf_files)
        st.session_state.vector_store = create_vector_store(text)
        st.success("Done!")

# Ask question
query = st.text_input("Ask question")

if query and st.session_state.vector_store:
    answer, pages = get_response(st.session_state.vector_store, query)

st.session_state.chat.append(("You", query))
st.session_state.chat.append(("Bot", answer + f"\n\n📄 Source Pages: {list(pages)}"))

# Show chat
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f'<div class="user-message">🧑 {msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">🤖 {msg}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Export
if st.button("Export Chat"):
    df = pd.DataFrame(st.session_state.chat, columns=["Speaker", "Message"])
    df.to_csv("chat.csv", index=False)
    st.success("Exported!")