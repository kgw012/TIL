from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField


class Review(models.Model):
    movie_title = CharField(max_length=100)
    title = CharField(max_length=100)
    content = TextField()
    rank = IntegerField()

    def __str__(self):
        return self.title
