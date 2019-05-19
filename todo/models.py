from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    create = models.DateField(auto_now=true)
    exp = models.DateTimeField()

    def __str__(self):
        return self.task
