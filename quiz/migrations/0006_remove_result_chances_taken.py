# Generated by Django 4.2.1 on 2023-08-22 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_quiz_quiz_chances_alter_result_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='chances_taken',
        ),
    ]