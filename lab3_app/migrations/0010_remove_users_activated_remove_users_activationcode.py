# Generated by Django 4.1.1 on 2022-12-20 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_app', '0009_game_managed_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='activated',
        ),
        migrations.RemoveField(
            model_name='users',
            name='activationCode',
        ),
    ]
