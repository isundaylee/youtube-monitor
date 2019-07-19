import requests
import datetime
import urllib

from bs4 import BeautifulSoup

from youtube_monitor.models import ChannelReading
from youtube_monitor.utils import parse_integer
from youtube_monitor.video_monitor import VideoMonitor


class ChannelMonitor:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def get_readings(self):
        print("Reading channel {}".format(self.channel_id))

        body = requests.get(
            "https://www.youtube.com/channel/{}/videos?view=0&sort=dd&flow=grid".format(
                self.channel_id
            )
        )
        soup = BeautifulSoup(body.content, "html.parser")

        name = soup.select_one('meta[property="og:title"]')["content"]
        subscribers = parse_integer(
            soup.select_one(
                ".yt-subscription-button-subscriber-count-branded-horizontal"
            ).text
        )

        readings = [
            ChannelReading(
                time=datetime.datetime.now(),
                channel_id=self.channel_id,
                name=name,
                subscribers=subscribers,
            )
        ]

        for video in soup.select(".yt-lockup-video"):
            video_id = video["data-context-item-id"]
            readings.extend(VideoMonitor(video_id).get_readings())

        return readings

