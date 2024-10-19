# layout.py
import streamlit as st

def feedback_form():
    st.sidebar.header("Feedback")
    with st.sidebar.form("feedback_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        feedback = st.text_area("Your Feedback")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.sidebar.success("Thank you for your feedback!")
