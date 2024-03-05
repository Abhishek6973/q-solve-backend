# Generated by Django 5.0.1 on 2024-03-03 16:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('about_me', models.CharField(blank=True, default='', max_length=100)),
                ('website_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('github_link', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_expert', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('total_upvote_count', models.IntegerField(default=0)),
                ('phone_num', models.CharField(blank=True, max_length=30, unique=True)),
                ('experience_level', models.CharField(choices=[('Student', 'Student'), ('Junior', 'Junior'), ('Mid_Level', 'Mid Level'), ('Senior', 'Senior'), ('Lead', 'Lead'), ('Manager', 'Manager')], default='Student', max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('content', models.TextField(blank=True)),
                ('likes', models.IntegerField(blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
