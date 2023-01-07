import os
import streamlit as st
from utils.streamlit_utils import load_cover_image
from utils.google_cloud_utils import list_bucket_folder, read_from_google_bucket


st.sidebar.image(load_cover_image())

st.title("Telegram")

st.header("Qui puoi navigare quello che ci mandiamo su Telegram")

st.text("")

st.subheader("Elenco di tutti gli audio disponibili")

available_audios = list_bucket_folder("telegram_api_data/audio")
available_audios = [audio_file_remote_path.split("/")[-1] for audio_file_remote_path in available_audios]

selected_audio = st.selectbox(
    "Scegli l'audio che vuoi ascoltare:",
    available_audios
)

audio_file = read_from_google_bucket('telegram_api_data/audio/' + selected_audio)

st.audio(audio_file)

st.text("")
