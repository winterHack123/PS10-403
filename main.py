from Transcript_DataFrame import get_transcript
from yt_download import download_youtube_videos
from vid_edit import create_vid
from Summary import Summary
from fetchTS import process_dataframe

url = input()

df,transcript = get_transcript(url)

sentences = Summary(transcript)

print(sentences)

timestamps = process_dataframe(df,sentences)

print(timestamps)

vid_info = download_youtube_videos([url])

create_vid(vid_info['height'], timestamps, len(sentences))