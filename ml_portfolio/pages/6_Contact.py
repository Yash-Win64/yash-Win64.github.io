import streamlit as st
import os
st.set_page_config(page_title="Contact – Yash", layout="wide")

# ✅ Load your CSS
css_path = os.path.join(os.path.dirname(__file__), "../assets/style.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Page Title
st.title("📬 Contact Me")

st.markdown("Please fill in the form below. Your message will be delivered instantly to my email using **EmailJS**.")

# ✅ Streamlit placeholder for dynamic message
success_placeholder = st.empty()

# ✅ Embed HTML & JS for EmailJS form
contact_form = """
<form id="contact-form">
  <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px;" />
  <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px;" />
  <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; height: 200px;"></textarea>
  <br><br>
  <input type="submit" value="Send Message" style="background-color: #4f8bf9; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-weight: bold;" />
</form>

<div id="status-message" style="margin-top: 20px; font-weight: bold;"></div>

<script src="https://cdn.jsdelivr.net/npm/emailjs-com@3/dist/email.min.js"></script>
<script>
  (function(){
    emailjs.init("luQU3k6pHolaLmIdx");
  })();

  document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    emailjs.sendForm('service_xx9h1qv', 'template_631v5gn', this)
      .then(function() {
        // ✅ Update status message inside the HTML (replaces alert)
        document.getElementById('status-message').innerHTML = "✅ Your message has been sent successfully!";
        document.getElementById('status-message').style.color = "#28a745";
        document.getElementById("contact-form").reset();
      }, function(error) {
        document.getElementById('status-message').innerHTML = "❌ Failed to send message. Try again.";
        document.getElementById('status-message').style.color = "#dc3545";
      });
  });
</script>
"""

# ✅ Render the form
st.components.v1.html(contact_form, height=600)


