import base64
import streamlit as st
from PIL import Image


@st.experimental_memo()
def load_cover_image():
    image = Image.open('telegram_api_data/images/6fuori_copertina.png')
    return image


def add_bg_from_local(image_file):

    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: 200px 127px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
