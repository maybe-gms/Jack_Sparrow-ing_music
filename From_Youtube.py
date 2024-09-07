from pytube import YouTube
#def a(url):
yt=YouTube('https://www.youtube.com/watch?v=ZMBJFI9VQEI')
s=yt.streams.get_highest_resolution()
s.download('C:\\Users\\hp\\Music')
#a('https://www.youtube.com/watch?v=4CyyRHBIowE')
