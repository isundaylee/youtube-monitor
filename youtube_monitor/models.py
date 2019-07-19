import peewee


class VideoReading(peewee.Model):
    time = peewee.DateTimeField()
    url = peewee.TextField()
    available = peewee.BooleanField()
    views = peewee.IntegerField()
    likes = peewee.IntegerField()
    dislikes = peewee.IntegerField()


def initialize_database(db):
    db.bind([VideoReading])
    db.create_tables([VideoReading])
