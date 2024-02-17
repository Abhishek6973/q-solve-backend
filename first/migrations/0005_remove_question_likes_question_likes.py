# Generated by Django 5.0.1 on 2024-02-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_remove_question_likes_question_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
