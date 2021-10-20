from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)