from django.db import models
from first.models import User

# Create your models here.
class KitModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.JSONField() 
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)