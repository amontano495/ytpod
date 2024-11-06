import feedparser
import yt_dlp
import json
import sys
from datetime import date,datetime
def main():
    url_file = open("urls","r")
    for rss_url in url_file:
    
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
                        'preferredcodec': 'mp3',
                    }]
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    error_code = ydl.download(URLS)
    sys.exit(0)

main()

'''
    print("From",delta,"days ago")
    print(entry.title)
    print(entry.link)
'''
