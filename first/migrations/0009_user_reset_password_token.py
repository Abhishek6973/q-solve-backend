# Generated by Django 5.0.1 on 2024-02-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0008_delete_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_password_token',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
