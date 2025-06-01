import yt_dlp
from time import sleep

def download_audio(url, name, download_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{download_path}/{name}.%(ext)s',  # Use the provided name for each file
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    sleep(1)

# Dictionary of songs with custom file names as keys and their YouTube URLs as values
url_dic = {
    #"name":"url",
    "Pularan Neram":"https://www.youtube.com/watch?v=nUugKaA1MYs",
    "Kayarillaakkettil Pettu":"https://www.youtube.com/watch?v=u8k_UtwvXAY",
    "Shilayude ":"https://www.youtube.com/watch?v=Ce36JRz72UE",
}

# Download path
download_path = 'C:\\Users\\hp\\Pendrive\\Android Kunjappan'

# Loop through the dictionary and download each song
for name, url in url_dic.items():
    print(f"Downloading: {name}")
    download_audio(url, name, download_path)
