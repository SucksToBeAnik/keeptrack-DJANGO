from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from account.models import Profile
# Create your models here.

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True)
    skill_type = models.ForeignKey('SkillType', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000,null=True,blank=True)
    skill_level = models.IntegerField(default=1)
    current_point = models.IntegerField(default=0)
    learning = models.BooleanField(default=True)
    started_learning = models.DateField(null=True,blank=True,auto_now_add=True)

    def __str__(self):
        return self.title

    def update_skill_level(self,exp):
        self.current_exp += exp
        if self.current_exp == 100:
            self.skill_level += 1
            self.current_exp = 0
        self.save()
    
    @property
    def needed_point(self):
        return self.skill_level*100 - self.current_point

class SkillType(models.Model):
    title = models.CharField(max_length=255)
    # skill_set

    def __str__(self):
        return self.title

class SkillObj(models.Model):
    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.SET_NULL)
    object_id = models.IntegerField()
    content_object = GenericForeignKey()

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.skill.title