from django.contrib import admin
from .models import Note, FeaturedNote

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','owner','created_at']