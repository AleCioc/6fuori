import os
import base64
import streamlit as st
from utils.streamlit_utils import load_cover_image
from utils.google_cloud_utils import list_bucket_folder, read_from_google_bucket


st.sidebar.image(load_cover_image())

available_audios = list_bucket_folder("telegram_api_data/audio")
available_audios = [audio_file_remote_path.split("/")[-1] for audio_file_remote_path in available_audios]

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

audio_file = read_from_google_bucket('telegram_api_data/audio/' + selected_song_audio)

st.audio(audio_file)

st.text("")

st.subheader("{} - testo e accordi".format(selected_song))

cols_tuple = tuple(
    [1 for i in range(len(list_bucket_folder("lyrics_with_chords_png/{} - testo e accordi".format(selected_song))))]
)
st_cols = st.columns(cols_tuple)
i = 0
for f in list_bucket_folder("lyrics_with_chords_png/{} - testo e accordi".format(selected_song)):
    lyrics_with_chords_image = read_from_google_bucket(
        "lyrics_with_chords_png/{} - testo e accordi/{}".format(selected_song, f.split("/")[-1]),
        mode="bytes"
    )
    st_cols[i].image(lyrics_with_chords_image, use_column_width=True)
    i += 1

# base64_pdf = base64.b64encode(
#     read_from_google_bucket(
#         "lyrics_with_chords/{} - testo e accordi.pdf".format(selected_song),
#         mode="bytes"
#     )
# ).decode('utf-8')
#
# pdf_display = F"""
#     <iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf"></iframe>
# """
#
# st.markdown(pdf_display, unsafe_allow_html=True)
#
# import streamlit as st
# import streamlit.components.v1 as components
#
# # components.iframe(
# #     "https://storage.googleapis.com/6fuori_telegram_data/lyrics_with_chords/{}".format(
# #         "{} - testo e accordi.pdf".format(selected_song)
# #     ),
# #     width=1050,
# #     height=1000,
# #     scrolling=True
# # )
