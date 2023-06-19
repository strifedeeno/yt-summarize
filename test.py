from transformers import pipeline
import yt_dlp
import whisper
import os
from transformers import pipeline, set_seed

URLS = input("Enter youtube video url: ")

ydl_opts = {
    'format': 'best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)

os.system("ren *mp3 audio.mp3")

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")

summarizer = pipeline("summarization", model="google/pegasus-cnn_dailymail")
print(summarizer(result["text"]))

os.remove("audio.mp3")