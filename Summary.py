from youtube_transcript_api import YouTubeTranscriptApi
import openai
import pandas as pd
import boto3

import nltk
nltk.download("punkt") 
url = 'https://www.youtube.com/watch?v=mwKJfNYwvm8'

video_id = url.replace('https://www.youtube.com/watch?v=', '')

transcript = YouTubeTranscriptApi.get_transcript(video_id)
print(transcript)
df=pd.DataFrame(transcript)
df['end'] = df['start'].shift(-1)
df = df.drop(df.index[-1])
df = df.drop('duration', axis=1)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)



def Summary(df):

    openai.api_key = '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'

    output=""
    for x in transcript:
        sentence=x['text']
        output=f'{output}{sentence}\n'

    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You have spoken as the assistant"},
            {"role":"assistant","content":"Write a 150-word and 7 lines of  summary of this video in the first person and present tense and you are the host in same paragraph "},
            {"role":"user","content":output}
        ]
    )
    summary=response["choices"][0]["message"]["content"]
    polly_client = boto3.Session(
                aws_access_key_id="AKIAUS2GZTU3OAIHXR7L",                     
    aws_secret_access_key="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",
    region_name='us-west-2').client('polly')
    sentences = nltk.sent_tokenize(summary)
    ind=1
    for sentence in sentences:
        response = polly_client.synthesize_speech(VoiceId='Stephen',
                    OutputFormat='mp3', 
                    Text = sentence,
                    Engine = 'neural')
        file = open('Speech/speech'+str(ind)+'.mp3', 'wb')
        ind=ind+1
        file.write(response['AudioStream'].read())
        file.close()
    printf("Finished")
    return sentences

Summary(df)























