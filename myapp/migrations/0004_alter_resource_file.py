# Generated by Django 4.2.1 on 2023-05-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_rename_start_date_course_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resource",
            name="file",
            field=models.FileField(blank=True, upload_to="resources/"),
        ),
    ]