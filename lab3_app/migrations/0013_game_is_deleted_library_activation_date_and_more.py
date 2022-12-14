# Generated by Django 4.1.1 on 2023-01-11 05:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_app', '0012_remove_game_genre_game_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='library',
            name='activation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='library',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='library',
            name='payment_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
