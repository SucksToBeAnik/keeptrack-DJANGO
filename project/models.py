from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from skill.models import SkillObj
from account.models import Profile
from note.models import Note

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True)
    skill = GenericRelation(SkillObj)
    note = GenericRelation(Note)
    title = models.CharField(max_length = 255)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    live_link = models.URLField(blank=True, null=True, max_length=500)
    code_link = models.URLField(blank=True, null=True, max_length=500)
    project_state = models.BooleanField(default=False)
    project_image = models.ImageField(null=True, blank =True, upload_to='keeptrack/images/')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']

