import datetime

from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    def __str__(self):
        return self.content
