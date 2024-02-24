from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone


EXPERIENCE_LEVEL = [

    ('Student','Student'),
    ('Junior', 'Junior'),
    ('Mid_Level', 'Mid Level'),
    ('Senior', 'Senior'),

]

ROLES =[
    ('User','User'),
    ('Expert','Expert'),
    ('Admin','Admin')
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
    role = models.CharField(max_length=30,choices=ROLES,default="User")
    is_active = models.BooleanField(default=False)
    total_upvote_count = models.IntegerField(default=0)
    phone_num = models.CharField(max_length=30, blank=True,null=True, unique=True)
    experience_level = models.CharField(max_length=30, choices=EXPERIENCE_LEVEL, default='Student')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password,self.password)
    def __str__(self):
        return self.email