import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Mingrammer Azure Architecture diagram",
    page_icon=":books:",
    layout="wide"
)
st.markdown("""
            <style>
                   [data-testid="block-container"] {
                        padding-top: 0.27rem;
                        padding-bottom: 6rem;
                        padding-left: 6rem;
                        padding-right: 6rem;
                    }
            </style>
            """, unsafe_allow_html=True)
st.write("")
if __name__ == "__main__":
    st.header('Azure Architecture (Diagram as Code)', divider='rainbow')
    st.selectbox(
        'service',
        ('AWS', 'Azure'))


    image_paths = {
        "web_service": "web_service.png",
        "tenant_secure_access_with_private_endpoints": "azure-app-services.png",
        "e commerce search":"ecommerce_search.png"
    }

    selected_option = st.empty()
    def display_image():
        print(selected_option)
        if selected_option:
            image_path = image_paths.get(selected_option)
            if image_path:
                st.image(image_path)
            else:
                st.info("No image available for this option.")

    selected_option = st.selectbox("Select an architecture diagram", list(image_paths.keys()))

    # Create a button
    button = st.button("Open Image")

    # Display image on button click
    if button:
        display_image()