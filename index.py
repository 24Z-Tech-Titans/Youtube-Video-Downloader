from tkinter import *
import tkinter.ttk as ttk
from pytube import YouTube

class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Youtube Video Downloader")
        self.label = ttk.Label(self.root, text="Youtube Video Downloader", font="Arial 30")
        self.frame = ttk.Frame(self.root)
        self.frame.grid(column=0, row=1)
        self.linklabel = ttk.Label(self.frame, text="Youtube Link:", font= "Arial 15")
        self.entry = ttk.Entry(self.frame, font="Arial 15", width=40)
        self.button = ttk.Button(self.frame, text="Download", width=20, command=self.download_yt_video)
        self.label.grid(pady=(150, 50), padx=150, column=0, row=0)
        self.linklabel.grid(pady=20, padx=0, column=0, row=1)
        self.entry.grid(pady=20, padx=0, column=1, row=1)
        self.button.grid(pady=20, padx=0, column=0, row=2)
           
    def download_yt_video(self):
        self.url = self.entry.get()
        yt = YouTube(self.url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        
    def run(self):
        self.root.mainloop()
        
my_app = App()
my_app.run()