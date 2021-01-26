import streamlit as st
import pickle
from fastai.text.all import *
import sentencepiece
import requests

st.title("Classify your (German) lyrics! :tada::microphone::notes:")

model = requests.get("https://github.com/tlary/genre-streamlit/blob/main/genreModel.pkl?raw=true")
learn_inf = load_learner(model)
#learn_inf = load_learner("genreModel.pkl")
images = "./static/"

expander = st.beta_expander("Lyrics")
with expander:
    lyrics = st.text_area("Paste your lyrics here:", height=100)
    clicked = st.button("Classify lyrics!")

if clicked:
    st.spinner("Predicting the song's genre...")
with st.beta_container():
    # make prediction and edit output format
    if clicked:
        with st.spinner("Predicting the song's genre..."):
            pred = learn_inf.predict(lyrics)[0]
            img = images + pred + ".jpg"
            # edit string output
            if pred == "hiphop":
                pred = "Hip-Hop"
            if pred in ["pop", "schlager"]:
                pred = pred.capitalize()
            st.image(img, use_column_width=True)
            st.info("The song's genre is " + pred)

import requests
model = requests.get("https://github.com/tlary/genre-streamlit/blob/main/genreModel.pkl?raw=true")
