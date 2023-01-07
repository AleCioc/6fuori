import os
import streamlit as st
from PIL import Image

image = Image.open('telegram_api_data/images/6fuori_copertina.png')
st.sidebar.image(image)

st.title("Telegram")

st.header("Qui puoi navigare quello che ci mandiamo su Telegram")

st.text("")

st.subheader("Elenco di tutti gli audio disponibili")
available_audios = os.listdir("telegram_api_data/audio")
selected_audio = st.selectbox(
    "Scegli l'audio che vuoi ascoltare:",
    available_audios
)

audio_file = open('telegram_api_data/audio/' + selected_audio, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_file)

st.text("")
