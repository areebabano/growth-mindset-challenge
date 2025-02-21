import streamlit as st
import requests
import re

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZlMDYzZTA0MzU1MjY1NTUzMzUxMzEi_pc"

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
         name = st.text_input("Name", "", max_chars=50)
         email = st.text_input("Email", "", max_chars=100)
         message = st.text_area("Your Message", "", max_chars=500)
         submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not WEBHOOK_URL:
            st.error(
                "Email service is not set up properly. Please try again later", icon="⚠️"
            )
            st.stop()

        if not name:
            st.error("Please enter your name" , icon="👤")
            st.stop()

        if not email:
            st.error("Please enter your email" , icon="✉")
            st.stop()

        if not message:
            st.error("Please provide a message" , icon="💌")
            st.stop()

        
        data = {"name": name, "email": email, "message": message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Message sent successfully! ✨", icon="🚀")
        else:
            st.error("There was an error sending your message", icon="😨")
            st.stop()

        

        