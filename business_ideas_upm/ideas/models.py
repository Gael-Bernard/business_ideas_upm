from sqlite3 import Date
from django.db import models

# Create your models here.
class BusinessIdea(models.Model):
    title = models.TextField(max_length=128)
    body = models.TextField(max_length=4096)
    username = models.TextField(max_length=32)
    publish_date = models.DateTimeField()


class IdeaComment(models.Model):
    idea = models.ForeignKey(BusinessIdea, on_delete=models.CASCADE)
    body = models.TextField(max_length=4096)
    username = models.TextField(max_length=32)
    publish_date = models.DateTimeField()