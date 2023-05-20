# Generated by Django 4.2.1 on 2023-05-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_announcement_created_announcement_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]