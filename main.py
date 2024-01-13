from pytube import YouTube
from sys import argv 
import os
from pathlib import Path

link = argv[1]
yt = YouTube(link)
video = yt.streams.filter(abr='160kbps').last()
file = video.download('/Users/Leon Liu/Downloads')
base, ext = os.path.splitext(file)
new_file = Path(f'{base}.mp3')
os.rename(file, new_file)
