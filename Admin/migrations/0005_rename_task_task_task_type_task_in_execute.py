# Generated by Django 4.0.1 on 2022-01-31 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_task_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='task_type',
        ),
        migrations.AddField(
            model_name='task',
            name='in_execute',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
