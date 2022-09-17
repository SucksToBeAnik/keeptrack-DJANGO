from django.contrib import admin
from .models import Profile,Inbox,Message

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username','bio']

@admin.register(Inbox)
class InobxAdmin(admin.ModelAdmin):
    list_display = ['owner']

admin.site.register(Message)
