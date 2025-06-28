import logging
import os
import queue
import sounddevice as sd
import soundfile as sf
from openai import OpenAI

from config_template import OPENAI_API_KEY, MODEL_TTS

client = OpenAI(api_key=OPENAI_API_KEY)

TEMP_PATH = "/tmp/tts_out.wav"


def play_wav(path: str):
    data, fs = sf.read(path, dtype="float32")
    sd.play(data, fs)
    sd.wait()


def tts_loop(answer_q: queue.Queue):
    while True:
        answer = answer_q.get()
        if answer is None:
            break
        try:
            with open(TEMP_PATH, "wb") as f:
                response = client.audio.speech.create(
                    model=MODEL_TTS,
                    voice="alloy",
                    input=answer,
                )
                f.write(response.content)
            play_wav(TEMP_PATH)
        except Exception as e:
            logging.error(f"TTS error: {e}")
            continue
        finally:
            if os.path.exists(TEMP_PATH):
                os.remove(TEMP_PATH)

