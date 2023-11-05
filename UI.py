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
# Set the title and background color
st.set_page_config(page_title="403 Hackathon Video", page_icon="🚀", layout="centered")

# Page title and description
st.title("403 Hackathon Team")
st.write("Welcome to our hackathon project. Please enter a YouTube video URL below to get started!")

# Input field for the video URL
video_url = st.text_input("Enter YouTube Video URL")

# Button to process the URL (you can add your processing logic here)
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

# Footer
st.markdown("---")
st.write("Team 403 - Hackathon Project")