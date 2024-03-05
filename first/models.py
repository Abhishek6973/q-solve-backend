from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import User


EXPERIENCE_LEVEL = [
    ('Student', 'Student'),
    ('Junior', 'Junior'),
    ('Mid_Level', 'Mid Level'),
    ('Senior', 'Senior'),
    ('Lead', 'Lead'),
    ('Manager', 'Manager'),
]

class UserManager(BaseUserManager):
    def create_user(self, email, name, phone_num, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone_num=phone_num, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_num, password):
        user = self.create_user(
            email,
            name=name,
            phone_num=phone_num,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user # Set is_superuser to True for superuser

# abhishek86649@gmail.com



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name = 'Email',
        max_length = 255,
        unique=True)
    name = models.CharField(max_length=30, default='', blank=True)
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

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_num']

    def check_password(self, raw_password):
        return raw_password == self.password

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    content = models.TextField(blank=True)
    likes = models.IntegerField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.email} - Question'

    def total_likes(self):
        return self.likes.count()
