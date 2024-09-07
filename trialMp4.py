import yt_dlp

def download_video(url, download_path):
    ydl_opts = {
        'format': 'best',  # Download the best available quality
        'merge_output_format': 'mp4',  # Ensure the output file is in MP4 format
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save files to the specified download path with the video title as the file name
        'noplaylist': True  # Download only the video, not the entire playlist if the URL is part of one
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Replace this URL with the URL of the YouTube video you want to download
url = 'https://www.youtube.com/watch?v=JtHKPpxGfRU&list=OLAK5uy_mY4skY5yDePaN61M2yFNp2s1SCaE6AHx8'
# Replace this with the path to the directory where you want to save the downloaded video
download_path = 'C:\\Users\\hp\\Music\\Il Ballo Della Vita'
download_video(url, download_path)

