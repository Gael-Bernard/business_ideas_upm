from django.db import models

# Create your models here.
class BusinessIdea(models.Model):
    title = models.TextField(max_length=128)
    body = models.TextField(max_length=4096)
    username = models.TextField(max_length=32)


class IdeaComment(models.Model):
    idea: models.ForeignKey(BusinessIdea, on_delete=models.CASCADE)
    title = models.TextField(max_length=128)
    body = models.TextField(max_length=4096)
    username = models.TextField(max_length=32)