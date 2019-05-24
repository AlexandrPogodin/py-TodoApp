from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100, blank=True)
    done = models.BooleanField(default = False)
    author = models.CharField(max_length = 50, default='')
    date = models.DateTimeField(auto_now = True)