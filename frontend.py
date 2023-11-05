from streamlit_lottie import st_lottie
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import openai
import pandas as pd
import boto3
import yt_dlp
from Transcript_DataFrame import get_transcript
from yt_download import download_youtube_videos
from vid_edit import create_vid
from Summary import Summary
from fetchTS import process_dataframe
import subprocess
import webbrowser

# ---- LOAD ASSETS ----
lottie_coding1 = "https://lottie.host/0cb996b4-4a94-480a-b0f3-4cb6508b4b94/dddajgyDoz.json"
lottie_coding2 = "https://lottie.host/1240fabd-1a2f-4c8b-baa3-18dc4dca7079/b3qCPSC1SU.json"

st.set_page_config(page_title="FinnCut", page_icon="🎬", layout="wide")



with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("🎬 FinnCut")
        st.subheader("LLM powered YT Short generator")
    with right_column:
        st_lottie(lottie_coding2, height=300, key="browsing")

video_url = st.text_input("Enter YouTube Video URL")
if st.button("Process Video"):
    if video_url:
        df,transcript = get_transcript(video_url)
        sentences = Summary(transcript)
        print(sentences)
        ss=""
        for sentence in sentences:
            ss+=sentence
        st.write("Summary")
        st.markdown(ss)
        st.write("Wait.....")
        timestamps = process_dataframe(df,sentences)
        print(timestamps)
        vid_info = download_youtube_videos([video_url])
        create_vid(vid_info['height'], timestamps, len(sentences))
        file_path = r'final.mp4'  # Replace with the path to your media file
        webbrowser.open(file_path)
    else:
        st.warning("Please enter a YouTube video URL.")
