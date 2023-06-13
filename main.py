import streamlit as st
import youtube_transcript_api

address = st.text_input("Input_youtube_address:")
st.write(youtube_transcript_api.get_transcript(address))