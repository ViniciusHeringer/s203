# Generated by Django 3.0.6 on 2020-06-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0011_movie_watch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watch',
        ),
        migrations.AddField(
            model_name='myrating',
            name='watch',
            field=models.BooleanField(default=False),
        ),
    ]