import peewee

from youtube_monitor import VideoMonitor
from youtube_monitor.models import initialize_database

DATABASE_PATH = "data.db"


def main():
    db = peewee.SqliteDatabase(DATABASE_PATH)
    initialize_database(db)

    test_url = "https://www.youtube.com/watch?v=FiyJf-8lMmo"
    monitor = VideoMonitor(test_url)

    for reading in monitor.get_readings():
        reading.save()


if __name__ == "__main__":
    main()
