import yt_dlp

def download_audio(url, download_path):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best available audio quality
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save files to the specified download path with the video title as the file name
        'noplaylist': True,  # Download only the video, not the entire playlist if the URL is part of one
        'postprocessors': [{  # Post-processors to convert the file to MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',  # Use the best available audio quality
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Replace this URL with the URL of the YouTube video you want to download
url = 'https://www.youtube.com/watch?v=HCXdiCj3vFk&list=OLAK5uy_l9U6SjFNumscmRFHxQkmhz2Ye8JPDiz0Q&index=2'
# Replace this with the path to the directory where you want to save the downloaded audio file
download_path = 'C:\\Users\\hp\\Music\\Eyes That See In The Dark - Kenny Rogers'
download_audio(url, download_path)
