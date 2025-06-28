import logging
import queue
import sounddevice as sd

def capture_audio(audio_q: queue.Queue, block_duration: float = 1.0):
    """Capture audio from microphone and put blocks into a queue."""
    samplerate = 16000
    blocksize = int(samplerate * block_duration)
    channels = 1

    def callback(indata, frames, time, status):
        if status:
            logging.warning(f"Input status: {status}")
        audio_q.put(indata.copy())

    try:
        with sd.InputStream(
            channels=channels,
            samplerate=samplerate,
            blocksize=blocksize,
            callback=callback,
        ):
            logging.info("Audio capture started")
            while True:
                sd.sleep(int(block_duration * 1000))
    except KeyboardInterrupt:
        logging.info("Audio capture stopped")

