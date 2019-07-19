import requests
import datetime
import urllib

from bs4 import BeautifulSoup

from youtube_monitor.models import *


def parse_integer(text):
    return int("".join(filter(lambda c: c != ",", text)))


class VideoMonitor:
    def __init__(self, url):
        self.url = url

    def get_readings(self):
        body = requests.get(self.url)
        soup = BeautifulSoup(body.content, "html.parser")

        video_id = urllib.parse.parse_qs(urllib.parse.urlparse(self.url).query)["v"][0]
        title = soup.select_one("title").text

        views = int(soup.select_one("meta[itemprop=interactionCount]")["content"])
        likes = parse_integer(
            soup.select_one(".like-button-renderer-like-button-unclicked span").text
        )
        dislikes = parse_integer(
            soup.select_one(".like-button-renderer-dislike-button-unclicked span").text
        )

        return [
            VideoReading(
                time=datetime.datetime.now(),
                video_id=video_id,
                title=title,
                available=True,
                views=views,
                likes=likes,
                dislikes=dislikes,
            )
        ]
