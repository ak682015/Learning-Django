from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class DownClass(models.Model):
    title = models.CharField(max_length = 1000)

    def __str__(self):
        return self.title
