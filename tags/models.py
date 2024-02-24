from django.db import models
from first.models import User

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=255)
    creator_id=models.ForeignKey(User,on_delete=models.CASCADE)