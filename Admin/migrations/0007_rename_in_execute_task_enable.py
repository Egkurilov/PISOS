# Generated by Django 4.0.1 on 2022-02-25 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_alter_task_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='in_execute',
            new_name='enable',
        ),
    ]
