from youtube_transcript_api import YouTubeTranscriptApi
import openai
import pandas as pd

url = 'https://www.youtube.com/watch?v=-Oc8Rgdb-7A'

video_id = url.replace('https://www.youtube.com/watch?v=', '')

transcript = YouTubeTranscriptApi.get_transcript(video_id)

df=pd.DataFrame(transcript)
df['end'] = df['start'].shift(-1)
df = df.drop(df.index[-1])
df = df.drop('duration', axis=1)
df['id'] = df.reset_index().index
print(df)