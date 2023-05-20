# Generated by Django 4.2.1 on 2023-05-19 08:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0014_rename_message_host_message_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="participants",
            field=models.ManyToManyField(
                blank=True, related_name="participants", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]