# Generated by Django 4.1.1 on 2023-01-11 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_app', '0013_game_is_deleted_library_activation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='activation_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
