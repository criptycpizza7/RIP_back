# Generated by Django 4.1.1 on 2022-12-05 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_app', '0002_alter_users_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='join_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]
