import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import torch

model, example_texts, languages, punct, apply_te = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                  model='silero_te')
address = st.text_input("Input_youtube_address:")
text = ""
source = YouTubeTranscriptApi.get_transcript(address, languages=['ru'])
for i in source:
    text=text+" "+i['text']
st.write(apply_te(text, lan='ru'))