import peewee


class ChannelReading(peewee.Model):
    time = peewee.DateTimeField()
    channel_id = peewee.TextField()
    name = peewee.TextField()
    subscribers = peewee.IntegerField()


class VideoReading(peewee.Model):
    time = peewee.DateTimeField()
    channel_id = peewee.TextField()
    video_id = peewee.TextField()
    title = peewee.TextField()
    available = peewee.BooleanField()
    views = peewee.IntegerField(null=True)
    likes = peewee.IntegerField(null=True)
    dislikes = peewee.IntegerField(null=True)


def initialize_database(db):
    db.bind([ChannelReading, VideoReading])
    db.create_tables([ChannelReading, VideoReading])
