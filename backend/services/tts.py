import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVEN_API_KEY")

def text_to_speech(text):
    try:
        url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

        headers = {
            "xi-api-key": API_KEY,
            "Content-Type": "application/json"
        }

        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1"
        }

        res = requests.post(url, json=data, headers=headers)

        if res.status_code == 200:
            return res.content
        else:
            print("TTS ERROR:", res.text)
            return b""

    except Exception as e:
        print("TTS FAIL:", e)
        return b""