from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)
    desc = models.CharField(max_length=500, default="default")

    def __str__(self):
        return self.title
