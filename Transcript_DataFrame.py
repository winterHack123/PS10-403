from youtube_transcript_api import YouTubeTranscriptApi
import openai
import pandas as pd

url = 'https://www.youtube.com/watch?v=2TL3DgIMY1g'
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)
df=pd.DataFrame(transcript)
print(df)