import os
import base64
import streamlit as st
from streamlit_utils.streamlit_utils import load_cover_image


st.sidebar.image(load_cover_image())
available_audios = os.listdir("telegram_api_data/audio")

st.sidebar.subheader("Scegli canzone")
selected_song = st.sidebar.selectbox(
    "Seleziona canzone di cui vuoi esplorare gli audio:",
    ["Wonko", "Fiore", "Panino di Hassan", "Bacioni a Saviano"]
)

st.title("Musica")

st.header("Scegli la canzone nel menu a sinistra e inizia ad ascoltare")

st.text("")

st.subheader("{} - audio disponibili".format(selected_song))

selected_song_audios = [
    audio_filename for audio_filename in available_audios
    if selected_song.split(" ")[0].lower() in audio_filename.lower()
]

selected_song_audio = st.selectbox(
    "Scegli l'audio che vuoi ascoltare:",
    selected_song_audios
)
audio_file = open('telegram_api_data/audio/' + selected_song_audio, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_file)

st.text("")

st.subheader("{} - testo e accordi".format(selected_song))

with open("lyrics_with_chords/{} - testo e accordi.pdf".format(selected_song), "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf">'
st.markdown(pdf_display, unsafe_allow_html=True)
