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


class ProjectList (models.Model):
    CI = models.CharField(max_length=255, default="CI0000000", blank=True, null=True)
    SubSystem = models.CharField(max_length=255, default="mySubsystem", blank=True, null=True)
    Fp_name = models.CharField(max_length=255, default="DEBET_CARD", blank=True, null=True)


class SettingsDelay(models.Model):
    name_of_system = models.CharField(max_length=255, default="CI0000000", blank=True, null=True)
    name_of_services = models.CharField(max_length=255, default=None, blank=True, null=True)
    delay_URL = models.CharField(max_length=255, default="http://localhost:8080/", blank=True, null=True)
    default_ms = models.CharField(max_length=255, default=1, blank=True, null=True)
    critical_ms = models.CharField(max_length=255, default=2.8, blank=True, null=True)


class SettingsCancelExternalApi(models.Model):
    name_of_system = models.CharField(max_length=255, default=None, blank=True, null=True)
    name_of_services = models.CharField(max_length=255, default=None, blank=True, null=True)
    delay_URL = models.CharField(max_length=255, default="http://localhost:8080/", blank=True, null=True)
    default_ms = models.CharField(max_length=255, default=1, blank=True, null=True)
    critical_ms = models.CharField(max_length=255, default=60, blank=True, null=True)



"""
Тесты -> модель
    Включить заглушку
    Выключить заглушку
    + Установить долгий отклик
    Остановить сервера WAS (Фича, добавить галочку остановить один сервер) 
    Запустить сервера WAS
    Отключить proxy Внешней системы
    Включить proxy Внешней системы
    Наполнить MQ очередь
    Очистить MQ очередь
    Запустить тест Jmeter
    Остановить тест Jmeter
"""