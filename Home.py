import os
import streamlit as st
from streamlit_utils.streamlit_utils import load_cover_image

st.set_page_config(layout="wide")

st.title("Benvenut* nel sito dei 6fuori!")

st.subheader("Naviga il menu per ascoltare e guardare di che si tratta, a tuo rischio e pericolo O.O")

st.text("")
st.text("")

st.image(load_cover_image())
