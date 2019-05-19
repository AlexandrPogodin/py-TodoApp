from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100, blank=True)
    done = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now = True)