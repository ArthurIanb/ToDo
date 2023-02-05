from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
