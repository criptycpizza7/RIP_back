# Generated by Django 4.1.1 on 2022-12-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_app', '0007_library'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]
