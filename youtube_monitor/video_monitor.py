import requests
import datetime
import urllib

from bs4 import BeautifulSoup

from youtube_monitor.models import *


def parse_integer(text):
    return int("".join(filter(lambda c: c != ",", text)))


class VideoMonitor:
    def __init__(self, video_id):
        self.video_id = video_id

    def get_readings(self):
        body = requests.get("https://www.youtube.com/watch?v={}".format(self.video_id))
        soup = BeautifulSoup(body.content, "html.parser")

        channel_id = soup.select_one(".yt-user-info a")["href"].split("/")[-1]
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
                channel_id=channel_id,
                video_id=self.video_id,
                title=title,
                available=True,
                views=views,
                likes=likes,
                dislikes=dislikes,
            )
        ]
