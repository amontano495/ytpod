import feedparser
import yt_dlp
import json
from datetime import date,datetime

rss_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UCH8JwgaHCkhdfERVkGbLl2g"
feed = feedparser.parse(rss_url)

current_date = date.today()

for entry in feed.entries:
    entry_date = datetime.strptime(entry.published[:10],'%Y-%m-%d').date()
    delta = int((current_date-entry_date).days)
    if delta <= 1:
        URLS = [entry.link]
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(URLS)

'''
    print("From",delta,"days ago")
    print(entry.title)
    print(entry.link)
'''
