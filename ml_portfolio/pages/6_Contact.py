import streamlit as st
import requests

st.title("📬 Contact Me")

st.markdown("Fill the form below to get in touch:")

with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if not name or not email or not message:
            st.warning("Please fill out all fields.")
        else:
            # Send email via EmailJS
            email_data = {
                'service_id': 'service_mppzinh',
                'template_id': 'template_631v5gn',
                'user_id': 'luQU3k6pHolaLmIdx',
                'template_params': {
                    'name': name,
                    'email': email,
                    'message': message
                }
            }

            response = requests.post(
                'https://api.emailjs.com/api/v1.0/email/send',
                json=email_data
            )

            if response.status_code == 200:
                st.success("✅ Your message has been sent successfully!")
            else:
                st.error("❌ Failed to send message. Please try again later.")
