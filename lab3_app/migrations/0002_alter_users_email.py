# Generated by Django 4.1.1 on 2022-12-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
