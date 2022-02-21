from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, default=None)


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)

