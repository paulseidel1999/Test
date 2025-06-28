import logging
import multiprocessing as mp
from threading import Thread
import queue

from audio_capture import capture_audio
from transcriber import transcribe_loop
from prompt_engine import llm_loop
from tts_player import tts_loop
import ui


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    mp.set_start_method('spawn')

    audio_q: queue.Queue = queue.Queue()
    text_q: queue.Queue = queue.Queue()
    answer_q: queue.Queue = queue.Queue()

    threads = []

    def start_threads():
        if threads:
            return
        threads.extend([
            Thread(target=capture_audio, args=(audio_q,), daemon=True),
            Thread(target=transcribe_loop, args=(audio_q, text_q), daemon=True),
            Thread(target=llm_loop, args=(text_q, answer_q), daemon=True),
            Thread(target=tts_loop, args=(answer_q,), daemon=True),
        ])
        for t in threads:
            t.start()
        logging.info("Threads started")

    def stop_threads():
        for q in (audio_q, text_q, answer_q):
            q.put(None)
        for t in threads:
            t.join(timeout=1)
        logging.info("Threads stopped")

    ui.run(start_threads, stop_threads, text_q, answer_q)


if __name__ == "__main__":
    main()

