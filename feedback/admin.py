from django.contrib import admin
from .models import Comment,Like
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['owner','body','created_at']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['owner','created_at']