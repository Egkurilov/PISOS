from django.db import models


# Create your models here.
class Settings(models.Model):
    name = models.CharField(max_length=255, default=None)
    value = models.CharField(max_length=255, default=None)


class Task(models.Model):
    task_type = models.TextChoices('Shell Script', 'Http request')
    name = models.CharField(max_length=255, default=None)
    project = models.CharField(max_length=255, default=None)
    date = models.CharField(max_length=255, default=None)
    time = models.CharField(max_length=255, default=None)
    task_type = models.CharField(blank=True, choices=task_type.choices, max_length=10)
    in_execute = models.CharField(max_length=255, default=None)