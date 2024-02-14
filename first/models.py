from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils import timezone


EXPERIENCE_LEVEL = [

    ('Student','Student'),
    ('Junior', 'Junior'),
    ('Mid_Level', 'Mid Level'),
    ('Senior', 'Senior'),
    ('Lead', 'Lead'),
    ('Manager', 'Manager'),

]

class User(models.Model):
    name = models.CharField(max_length=30, default='', blank=True)
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    password = models.CharField(max_length=100)
    about_me = models.CharField(max_length=100, default='', blank=True)
    website_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_expert = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    total_upvote_count = models.IntegerField(default=0)
    phone_num = models.CharField(max_length=30, blank=True, unique=True)
    experience_level = models.CharField(max_length=30, choices=EXPERIENCE_LEVEL, default='Student')
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return raw_password == self.password
    def __str__(self):
        return self.email

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    content = models.TextField(blank = True)
    likes = models.IntegerField(blank = True)
    date_created = models.DateTimeField(default=timezone.now)   
    
    def __str__(self):
        return f'{self.user.username} - Question'
    
    def total_likes(self):
        return self.likes.count() 