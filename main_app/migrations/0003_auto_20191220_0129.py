# Generated by Django 2.2.6 on 2019-12-20 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20191218_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinking',
            old_name='drink',
            new_name='time',
        ),
    ]
