import tkinter
from tkinter import ttk
from pytube import YouTube
import customtkinter as ctk
import os

def dw_video():
    url= entry_url.get()
    resolution=res_var.get()
    progress_bar.pack(padx="10p",pady="5p")
    progress_label.pack(padx="10p",pady="5p")
    status_label.pack(padx="10p",pady="5p")
    try:
        yt= YouTube(url, on_progress_callback=on_progress)
        stream=yt.streams.filter(resolution=resolution).first()
        os.path.join("downloads",f"{yt.title}.mp4")
        stream.download(output_path="downloads")
        status_label.configure(text="Succesfully downloaded!", text_color="white", fg_color="green")
    except Exception as error:
        status_label.configure(text=f"Error {str(error)}",text_color="white",fg_color="red")

def dw_audio():
    url = entry_url.get()
    resolution = res_var.get()
    progress_bar.pack(padx="10p", pady="5p")
    progress_label.pack(padx="10p", pady="5p")
    status_label.pack(padx="10p", pady="5p")
    try:
        yt=YouTube(url, on_progress_callback=on_progress)
        stream=yt.streams.filter(only_audio=True).first()
        os.path.join("downloads",f"{yt.title}.mp4")
        stream.download(output_path="downloads")
        status_label.configure(text="Succesfully downloaded!", text_color="white", fg_color="green")
    except Exception as error:
        status_label.configure(text=f"Error {str(error)}", text_color="white", fg_color="red")


def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100
    progress_label.configure(text=str(int(percentage_completed))+"%")
    progress_label.update()
    progress_bar.set(float(percentage_completed/100))

root = ctk.CTk()
root.title("Youtube Downloader")
root.geometry("720x420")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
content_frame=ctk.CTkFrame(root)
content_frame.pack(expand=True, fill="both")

url_label=ctk.CTkLabel(content_frame, text="Youtube URL: ")
entry_url=ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(padx="10p",pady="10p")
entry_url.pack(padx="10p",pady="10p")

dw_button=ctk.CTkButton(content_frame, text="Download",command=dw_video)
dw_button.pack(padx="10p",pady="10p")

resolutions=["720p","360p","240p"]
res_var=ctk.StringVar()
res_combobox=ttk.Combobox(content_frame, values=resolutions,textvariable=res_var)
res_combobox.pack(padx="5p",pady="5p")
res_combobox.set("720p")

dw_audio_button=ctk.CTkButton(content_frame, text="Download audio",command=dw_audio)
dw_audio_button.pack(padx="10p",pady="10p")

progress_label=ctk.CTkLabel(content_frame, text="0%")

progress_bar=ctk.CTkProgressBar(content_frame,width=400)
progress_bar.set(0)

status_label=ctk.CTkLabel(content_frame, text="")



root.mainloop()