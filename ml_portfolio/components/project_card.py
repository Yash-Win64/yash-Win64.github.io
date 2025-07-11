import streamlit as st
from pathlib import Path

def project_card(title, description, link=None, image=None, github=None, tags=[]):
    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])

    with col1:
        fallback_image = "assets/images/default_project.png"
        image_path = Path(image) if image and Path(image).is_file() else Path(fallback_image)
        st.image(str(image_path), use_container_width=True)

    with col2:
        st.markdown(f"### {title}")
        st.markdown(description)

        if tags:
            st.markdown("**Tags:** " + " | ".join(tags))

        if link:  # link should be actual page filename like: "pages/3_Movie_Recommendation_System.py"
            if st.button(f"🔗 Live Demo – {title}"):
                st.switch_page(link)

        if github:
            st.markdown(
                f'<a href="{github}" class="project-btn" target="_blank">💻 Source Code</a>',
                unsafe_allow_html=True,
            )

    st.markdown('</div>', unsafe_allow_html=True)
