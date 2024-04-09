from tkinter import *
import tkinter.ttk as ttk
from pytube import YouTube

class App:
    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root, text="Youtube Downloader", font="Arial 40",foreground= "black")
        self.label.pack(pady=("250p", "5p"))
        
        self.entry = Entry(self.root,width=90,bd="2",relief="solid")
        self.entry.pack(pady=("10p", "5p"),ipady=("5p"))
        
        self.button = Button(self.root,text="Download",foreground="white",background="green",font="20",border="3",command=self.download_yt_video)
        self.button.pack(pady=("10p"),ipadx=("50p"),ipady=("5p"))
        
        self.resolutions = ["720px", "360px", "240px"]
        self.resolution_var = StringVar
        self.resolution_combobox = ttk.Combobox(values=self.resolutions,textvariable=self.resolution_var)
        self.resolution_combobox.pack(pady=("10p","5p"))
        self.resolution_combobox.set("720px")
        
        self.progress_label = Label(text="0%")
        
        self.status_label = Label(text="Downloaded")
        
           
    def download_yt_video(self):
        self.url = self.entry.get()
        yt = YouTube(self.url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        
    def run(self):
        self.root.mainloop()
        
my_app = App()
my_app.run()