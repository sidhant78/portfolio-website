import streamlit as st
from send_email import gmailer
st.title("Contact Me")
with st.form(key="email"):
    user_mail = st.text_input('Enter your Email address')
    message = st.text_area("your message")
    message = f"""\
    subject: New message from {user_mail}
    
from: {user_mail}
{message}"""
    button = st.form_submit_button('Submit')
    if button:
        gmailer(message)
        st.info('your email was sent successfully')
