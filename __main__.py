import peewee

from youtube_monitor import ChannelMonitor, VideoMonitor
from youtube_monitor.models import initialize_database

DATABASE_PATH = "data.db"


def main():
    db = peewee.SqliteDatabase(DATABASE_PATH)
    initialize_database(db)

    test_video_id = "FiyJf-8lMmo"
    test_channel_id = 'UCdXqCN_HtF_RjlsHzDSnJIQ'
    monitor = ChannelMonitor(test_channel_id)

    for reading in monitor.get_readings():
        reading.save()


if __name__ == "__main__":
    main()
