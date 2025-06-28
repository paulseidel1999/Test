import logging
import queue
from openai import OpenAI

from config_template import OPENAI_API_KEY, MODEL_CHAT

client = OpenAI(api_key=OPENAI_API_KEY)
SYSTEM_PROMPT = (
    "Du bist ein Meeting-Assistent. Fasse in 15 W\xC3\xB6rtern zusammen "
    "oder erg\xC3\xA4nze fehlende Zahlen/Fakten, falls sinnvoll."
)

full_transcript = ""
MAX_LEN = 4000

def llm_loop(text_q: queue.Queue, answer_q: queue.Queue):
    global full_transcript
    while True:
        text = text_q.get()
        if text is None:
            break
        full_transcript += " " + text
        full_transcript = full_transcript[-MAX_LEN:]
        logging.info(f"Prompting LLM with: {text}")
        try:
            stream = client.chat.completions.create(
                model=MODEL_CHAT,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": full_transcript},
                ],
                stream=True,
                max_tokens=32,
                temperature=0.3,
            )
            answer = ""
            for chunk in stream:
                if chunk.choices[0].finish_reason is not None:
                    break
                delta = chunk.choices[0].delta.content
                if delta:
                    answer += delta
            answer = answer.strip()
            logging.info(f"LLM: {answer}")
            answer_q.put(answer)
        except Exception as e:
            logging.error(f"LLM error: {e}")
            continue

