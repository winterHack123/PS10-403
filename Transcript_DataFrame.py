from youtube_transcript_api import YouTubeTranscriptApi
import openai
import pandas as pd

url = 'https://www.youtube.com/watch?v=-Oc8Rgdb-7A'
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)
print(transcript)
df=pd.DataFrame(transcript)
df['end'] = df['start'].shift(-1)
df = df.drop(df.index[-1])
df = df.drop('duration', axis=1)
print(df)