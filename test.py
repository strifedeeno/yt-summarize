from transformers import pipeline
import yt_dlp
import whisper
import os

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

os.system("mv *mp3 audio.mp3")

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")

summarizer = pipeline("summarization", model="facebook/bart-base")

print(summarizer(result['text'], max_length=1000, min_length=50, do_sample=False))

os.remove("audio.mp3")