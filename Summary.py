import openai
import pandas as pd
import boto3
import nltk

def Summary(transcript):

    #nltk.download('punkt')
    print('Downloaded')

    openai.api_key = '*'

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
    print(summary)

    polly_client = boto3.Session(
                aws_access_key_id="*",                     
    aws_secret_access_key="*",
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
    print("Finished")
    return sentences






















