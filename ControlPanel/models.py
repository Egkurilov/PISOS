from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, default=None)


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)
    CI = models.CharField(max_length=255, default="CI0000000", blank=True, null=True)
    SubSystem = models.CharField(max_length=255, default="mySubsystem", blank=True, null=True)
    Fp_name = models.CharField(max_length=255, default="DEBET_CARD", blank=True, null=True)
