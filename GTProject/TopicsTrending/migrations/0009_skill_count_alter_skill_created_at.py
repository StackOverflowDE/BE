# Generated by Django 5.0.4 on 2024-04-17 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopicsTrending', '0008_remove_job_skill_remove_skill_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='skill',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
