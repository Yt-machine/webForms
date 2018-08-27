from django.contrib import admin
from .models import Mood, Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)

class MoodAdmin(admin.ModelAdmin):
    list_display = ('status',)

admin.site.register(Mood,MoodAdmin)
admin.site.register(Post, PostAdmin)
