import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Plastic Waste Detection",
    page_icon="♻️",
    layout="wide"
)

st.title("♻️ Intelligent Plastic Waste Detection")
st.write("AI-powered plastic waste detection and environmental action system")

uploaded_file = st.file_uploader(
    "Upload a waste image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.success("Image uploaded successfully!")

    st.subheader("🌱 Environmental Action")
    st.info(
        "The system will analyze the image and recommend an appropriate "
        "environmental action."
  )
