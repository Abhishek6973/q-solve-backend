# Generated by Django 5.0.1 on 2024-02-24 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_alter_user_experience_level_alter_user_phone_num'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
