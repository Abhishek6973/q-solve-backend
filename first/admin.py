from django.contrib import admin
from .models import User,Question
# Register your models here.

class useradmin(admin.ModelAdmin):
    list_display = ( "email", "experience_level")

admin.site.register(User)
admin.site.register(Question)