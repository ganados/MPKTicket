import tkinter as tk
from tkinter import ttk


class ProgressBar(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.button = ttk.Button(text="start", command=self.start)
        self.button.pack()
        self.progress = ttk.Progressbar(self, orient="horizontal", length=100, mode="determinate")

        self.progress.pack()
        self.stored = 0
        self.max_stored


# TODO: ProgressBar if needed, consider
