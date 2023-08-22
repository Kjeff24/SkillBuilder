# Generated by Django 4.2.1 on 2023-08-22 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_result_started_result_chances_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_chances',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='result',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='quiz.quiz'),
        ),
    ]
