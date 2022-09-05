from django.contrib import admin
from .models import Skill, SkillType, SkillObj

# Register your models here.

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title','skill_level','skill_type']

@admin.register(SkillType)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(SkillObj)
class SkillObjAdmin(admin.ModelAdmin):
    list_display = ['skill']
