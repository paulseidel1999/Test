import logging
import queue
import io
import soundfile as sf
from openai import OpenAI

from config_template import OPENAI_API_KEY, MODEL_ASR

client = OpenAI(api_key=OPENAI_API_KEY)


def transcribe_loop(audio_q: queue.Queue, text_q: queue.Queue):
    """Consume audio blocks and produce text."""
    while True:
        block = audio_q.get()
        if block is None:
            break
        try:
            with io.BytesIO() as buffer:
                sf.write(buffer, block, 16000, format="WAV")
                buffer.seek(0)
                response = client.audio.transcriptions.create(
                    model=MODEL_ASR,
                    file=buffer,
                    response_format="text",
                )
            text = response
            logging.info(f"ASR: {text}")
            text_q.put(text)
        except Exception as e:
            logging.error(f"Transcription error: {e}")
            continue

