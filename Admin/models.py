from django.db import models


# Create your models here.
from Square.models import Project


class Settings(models.Model):
    name = models.CharField(max_length=255, default=None)
    value = models.CharField(max_length=255, default=None)


class TaskType(models.Model):
    type = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None, blank=True, null=True)


class Task(models.Model):
    name = models.CharField(max_length=255, default=None)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    enable = models.CharField(max_length=255, default=None, blank=True, null=True)