import streamlit as st
from pathlib import Path

def project_card(title, description, link=None, image=None, github=None, tags=[]):
    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])

    with col1:
        fallback_image = "assets/images/default_project.png"

        # ✅ Safely check if image exists
        image_path = Path(image) if image and Path(image).is_file() else Path(fallback_image)

        # ✅ Always show fallback if needed
        st.image(str(image_path), use_container_width=True)

    with col2:
        st.markdown(f"### {title}")
        st.markdown(description)

        if tags:
            st.markdown("**Tags:** " + " | ".join(tags))

        # Render Live Demo and GitHub links
       
        btn_html = ""
        if link:
            btn_html += f'<a href="{link}" target="_self" class="project-btn">🔗 Live Demo</a> '
        if github:
            btn_html += f'<a href="{github}" target="_blank" class="project-btn">💻 Source Code</a>'
        if btn_html:
            st.markdown(btn_html, unsafe_allow_html=True) 
       


    st.markdown('</div>', unsafe_allow_html=True)
