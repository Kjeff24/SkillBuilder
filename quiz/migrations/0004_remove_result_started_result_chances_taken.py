# Generated by Django 4.2.1 on 2023-08-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_quiz_end_date_alter_quiz_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='started',
        ),
        migrations.AddField(
            model_name='result',
            name='chances_taken',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
