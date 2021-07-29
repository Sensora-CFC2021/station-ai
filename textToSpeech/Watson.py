from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os


api_key = os.getenv('WATSON_API_KEY')
api = IAMAuthenticator(api_key)

text_to_speech = TextToSpeechV1(authenticator=api)
url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/5293fe37-deff-4f5f-b612-8700a570037a"
text_to_speech.set_service_url(url)


def text2speech(text):
    with open("test.mp3", "wb") as audio_file:
        audio_file.write(
            text_to_speech.synthesize(text, accept="audio/mp3").get_result().content
        )
