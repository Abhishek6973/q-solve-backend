from django.contrib import admin
from .models import User, Question

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone_num', 'is_expert', 'is_active', 'experience_level')
    list_filter = ('is_expert', 'is_active', 'experience_level')
    search_fields = ('email', 'name', 'phone_num')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'about_me', 'website_link', 'twitter_link', 'github_link', 'phone_num', 'experience_level')}),
        ('Permissions', {'fields': ('is_active', 'is_expert')}),
        ('Important dates', {'fields': ('created_at',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone_num', 'password1', 'password2'),
        }),
    )

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_created')
    search_fields = ('title', 'user__email')
    list_filter = ('date_created',)
