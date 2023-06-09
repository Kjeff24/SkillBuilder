# Generated by Django 4.2.1 on 2023-06-12 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0006_alter_resource_file_type"),
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="course",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="course.course",
            ),
        ),
    ]
