from tkinter import *
from customtkinter import *
from tkinter import filedialog as fd
from pytube import YouTube

class App:
    def __init__(self):
        self.root = CTk()
        self.root.geometry("700x700")
        self.root.title("Youtube Video Downloader")
        self.label = CTkLabel(self.root, text="Youtube Downloader", font=("Arial", 30), pady=90)
        self.label.pack()
        
        self.entry = CTkEntry(self.root, width=400, height=30, placeholder_text="Enter a URL")
        self.entry.pack()
        
        self.button = CTkButton(self.root, text="Download", command=self.download_yt_video)
        self.button.pack()
        
        # self.progress_label = CTkLabel(text="0%")
        
        # self.status_label = CTkLabel(text="Downloaded")
        
    def browse_location(self):
        # Work on the browsing location here with a browse button and the file dialog.
        pass
        
    
    def download_yt_video(self):
        try:
            self.url = self.entry.get()
            self.yt = YouTube(self.url)
            stream = self.yt.streams.get_highest_resolution()
            destination_folder = fd.askdirectory()
            if destination_folder:
                stream.download(destination_folder)
        except Exception as e:
            self.err_label = CTkLabel(self.root, text="Enter a valid URL")
            self.err_label.pack()
            

    def run(self):
        self.root.mainloop()
        
my_app = App()
my_app.run()