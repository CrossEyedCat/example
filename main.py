import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

address = st.text_input("Input_youtube_address:")
text = ""
for i in YouTubeTranscriptApi.get_transcript(address, languages=['ru']):
    text.__add__(i["text"])
st.write(text)