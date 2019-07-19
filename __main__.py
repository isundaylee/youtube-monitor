import peewee
import argparse

from youtube_monitor import ChannelMonitor
from youtube_monitor.models import initialize_database

DATABASE_PATH = "data.db"


def main():
    parser = argparse.ArgumentParser(
        description="Gather information of a YouTube channel and its newest videos."
    )
    parser.add_argument(
        "db_path",
        type=str,
        help="path to an SQLite database to save results into.",
    )
    parser.add_argument(
        "channel_id",
        type=str,
        help="ID of the channel to gather information of.",
    )

    args = parser.parse_args()

    db = peewee.SqliteDatabase(args.db_path)
    initialize_database(db)

    for reading in ChannelMonitor(args.channel_id).get_readings():
        reading.save()


if __name__ == "__main__":
    main()
