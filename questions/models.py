from django.db import models
from first.models import User
from django.utils import timezone
from tags.models import Tag

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.JSONField(blank = True)
    created_at = models.DateTimeField(default=timezone.now)  
    tags = models.ManyToManyField(Tag) 
    