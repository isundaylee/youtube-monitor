import requests
import datetime

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

        views = int(soup.select_one("meta[itemprop=interactionCount]")["content"])
        likes = parse_integer(
            soup.select_one(".like-button-renderer-like-button-unclicked span").text
        )
        dislikes = parse_integer(
            soup.select_one(".like-button-renderer-dislike-button-unclicked span").text
        )

        return [
            VideoReading(
                url=self.url,
                time=datetime.datetime.now(),
                available=True,
                views=views,
                likes=likes,
                dislikes=dislikes,
            )
        ]
