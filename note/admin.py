from django.contrib import admin
from .models import Note, FeaturedNote,BookmarkedNote

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','owner','created_at']

@admin.register(FeaturedNote)
class FeaturedNoteAdmin(admin.ModelAdmin):
    list_display = ['note']

admin.site.register(BookmarkedNote)