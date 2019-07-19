import peewee


class VideoReading(peewee.Model):
    time = peewee.DateTimeField()
    video_id = peewee.TextField()
    title = peewee.TextField()
    available = peewee.BooleanField()
    views = peewee.IntegerField(null=True)
    likes = peewee.IntegerField(null=True)
    dislikes = peewee.IntegerField(null=True)


def initialize_database(db):
    db.bind([VideoReading])
    db.create_tables([VideoReading])
