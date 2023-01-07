import base64
import streamlit as st
from PIL import Image
from utils.google_cloud_utils import read_from_google_bucket


@st.experimental_memo()
def load_cover_image():

    file_from_bucket = read_from_google_bucket(
        "telegram_api_data/images/6fuori_copertina.png"
    )

    image = Image.open(file_from_bucket)
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
