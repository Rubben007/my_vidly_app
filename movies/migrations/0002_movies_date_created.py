# Generated by Django 4.2.7 on 2023-11-22 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
