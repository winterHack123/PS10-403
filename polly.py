import boto3

polly_client = boto3.Session(
                aws_access_key_id="AKIAUS2GZTU3OAIHXR7L",                     
    aws_secret_access_key="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",
    region_name='us-west-2').client('polly')

response = polly_client.synthesize_speech(VoiceId='Stephen',
                OutputFormat='mp3', 
                Text = 'This is a sample text to be synthesized.',
                Engine = 'neural')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()