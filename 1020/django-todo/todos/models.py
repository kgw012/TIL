from django.db import models
from django.conf import settings


class Todo(models.Model):
    title = models.TextField()
    completed = models.BooleanField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
