"""Streamlit interface for the Magic 8-Ball project."""

import streamlit as st
from magic8 import get_answer

st.set_page_config(page_title="Magic 8-Ball", page_icon="🎱")
st.title("🎱 Magic 8-Ball")
st.write("Ask a yes-or-no question and discover your fortune!")

with st.form("magic8_form"):
    name = st.text_input("Your name (optional)")
    question = st.text_input("Your yes-or-no question")
    submitted = st.form_submit_button("Ask the Magic 8-Ball")

if submitted:
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        st.write(f"{name.strip()} asks: {question.strip()}" if name.strip() else f"Question: {question.strip()}")
        st.success(f"Magic 8-Ball's answer: {get_answer()}")
