import logging
import queue
import tkinter as tk
from tkinter import scrolledtext


def run(start_cb, stop_cb, text_q: queue.Queue, answer_q: queue.Queue):
    root = tk.Tk()
    root.title("Audio Copilot")
    root.geometry("400x300")

    transcript_box = scrolledtext.ScrolledText(root, bg="#f0f0f0", height=8)
    transcript_box.pack(fill=tk.BOTH, expand=True)

    answer_box = scrolledtext.ScrolledText(root, bg="white", height=4)
    answer_box.pack(fill=tk.BOTH, expand=True)

    def poll_queues():
        try:
            while True:
                text = text_q.get_nowait()
                transcript_box.insert(tk.END, text + "\n")
                transcript_box.see(tk.END)
        except queue.Empty:
            pass
        try:
            while True:
                ans = answer_q.get_nowait()
                answer_box.insert(tk.END, ans + "\n")
                answer_box.see(tk.END)
        except queue.Empty:
            pass
        root.after(100, poll_queues)

    def on_start():
        logging.info("UI start pressed")
        start_cb()

    def on_stop():
        logging.info("UI stop pressed")
        stop_cb()
        root.destroy()

    start_btn = tk.Button(root, text="Start", command=on_start)
    start_btn.pack(side=tk.LEFT, expand=True, fill=tk.X)
    stop_btn = tk.Button(root, text="Stop", command=on_stop)
    stop_btn.pack(side=tk.RIGHT, expand=True, fill=tk.X)

    root.after(100, poll_queues)
    root.mainloop()

