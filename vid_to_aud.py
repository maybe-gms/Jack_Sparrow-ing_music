from moviepy.editor import *
import os

def v(path,name):
    video = VideoFileClip(path)
    a = video.audio
    name="D:\\PenDrive 2.0\\Il Ballo Della Vita\\"+name+".mp3"
    a.write_audiofile(name)
    video.close()
    os.remove(path)

#C:\Users\hp\Music\Eyes That See In The Dark - Kenny Rogers
v("D:\\PenDrive 2.0\\Il Ballo Della Vita\\New Song.mp4","New Song")