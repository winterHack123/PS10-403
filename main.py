from Transcript_DataFrame import get_transcript
from yt_download import download_youtube_videos
from vid_edit import create_vid

url = input()

df = get_transcript(url)

vid_info = download_youtube_videos([url])

create_vid(vid_info['height'], df)

