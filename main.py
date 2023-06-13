import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

address = st.text_input("Input_youtube_address:")
text = ""
source = YouTubeTranscriptApi.get_transcript(address, languages=['ru'])
for i in source:
    text=text+i['text']
st.write(text)