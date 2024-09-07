from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up the WebDriver with WebDriver Manager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Open the Spotify playlist URL
playlist_url = 'https://open.spotify.com/album/0Rkv5iqjF2uenfL0OVB8hg'  # Update with your playlist URL
driver.get(playlist_url)

# Wait for the page to load and scroll down
time.sleep(5)  # Wait for 5 seconds

# Scroll down to load more songs (you can adjust the number of scrolls)
for _ in range(5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

# Get the page source and close the WebDriver
page_source = driver.page_source
# Parse the page source with Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')
driver.quit()

# Parse the page source with Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract song information
songs = []
for item in soup.select('div', {'class': 'tracklist-row name'}):
    song_title = item.select_one('span', {'class': 'track-name'}).text.strip()
    artist_name = item.select_one('span', {'class': 'artists-albums'}).text.strip()
    songs.append({'title': song_title, 'artist': artist_name})

# Print the song information
for song in songs:
    print(f"Title: {song['title']}, Artist: {song['artist']}")