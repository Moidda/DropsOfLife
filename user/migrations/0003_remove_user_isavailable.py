# Generated by Django 3.0.7 on 2022-02-17 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220218_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='isAvailable',
        ),
    ]
