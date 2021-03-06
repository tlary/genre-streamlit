import streamlit as st
import pickle
from fastai.text.all import *
import sentencepiece
import requests
from io import BytesIO

st.title("Classify your (German) lyrics! :tada::microphone::notes:")

# download model from Dropbox, cache it and load the model into the app
@st.cache(allow_output_mutation=True)
def load_model(url):
    modelLink = url
    model = requests.get(modelLink).content
    return model
modelFile = load_model("https://www.dl.dropboxusercontent.com/s/v6ezoyjpibrzjvu/genreModel.pkl?dl=0")
model = BytesIO(modelFile)
learn_inf = load_learner(model)

# point to the images
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

