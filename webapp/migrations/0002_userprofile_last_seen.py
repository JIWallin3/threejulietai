# Generated by Django 4.2 on 2023-04-19 19:11

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="last_seen",
            field=models.DateTimeField(
                auto_now=True, verbose_name=django.contrib.auth.models.User
            ),
        ),
    ]