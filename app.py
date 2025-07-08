import streamlit as st
from logic import generate_questions
from prompts import greeting_message, farewell_message

st.set_page_config(page_title="Hiring Assistant", layout="centered")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [greeting_message()]

st.title("🤖 AI Hiring Assistant - TalentScout")

with st.form("candidate_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0)
    position = st.text_input("Desired Position")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack (e.g., Python, React, MySQL)")
    submitted = st.form_submit_button("Start Screening")

if submitted:
    st.session_state.messages.append(f"👤 {name} submitted details.")
    with st.spinner("Generating questions..."):
        questions = generate_questions(name, tech_stack)
    st.session_state.messages.append(questions)

st.subheader("💬 Chat History")
for msg in st.session_state.messages:
    st.markdown(msg)

if st.button("End Conversation"):
    st.session_state.messages.append(farewell_message())
    st.rerun()
