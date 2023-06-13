import streamlit as st

from youtube_transcript_api import YouTubeTranscriptApi

address = st.text_input("Input_youtube_address:")
st.write(YouTubeTranscriptApi.get_transcript(address))