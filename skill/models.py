from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from account.models import Profile
from note.models import Note

from django.contrib import messages
# Create your models here.

class Skill(models.Model):
    SKILL_TYPE_CHOICES = (
        ('Programming Language','Programming Language'),
        ('Database','Database'),
        ('Hosting Platform','Hosting Platform'),
        ('Coding Utility','Coding Utility'),
        ('Frontend Framework','Frontend Framework'),
        ('Backend Framework','Backend Framework'),
        ('Machine Learning Tool','Machine Learning Tool'),
        ('Data Science Tool','Data Science Tool'),
        ('Artificial Intelligence Tool','Artificial Intelligence Tool')
    )
    skill_type = models.CharField(max_length=200,choices=SKILL_TYPE_CHOICES,null=True,blank=True)

    note = GenericRelation(Note)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True,default="Coding Utility")
    
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500,null=True,blank=True)
    skill_level = models.IntegerField(default=1)
    current_point = models.IntegerField(default=0)
    learning = models.BooleanField(default=True)
    started_learning = models.DateField(null=True,blank=True,auto_now_add=True)

    def __str__(self):
        return self.title

    def update_skill_level(self,request,point):
        self.current_point += point
        if self.current_point == (self.skill_level*50):
            self.skill_level += 1
            self.current_point = 0
            messages.success(request, f"Congratulations! You have recahed level {self.skill_level} in {self.title}. Keep grinding! you will reach there.")

        self.save()
    
    @property
    def needed_point(self):
        return self.skill_level*50 - self.current_point

# class SkillType(models.Model):
#     title = models.CharField(max_length=255)
#     # skill_set

#     def __str__(self):
#         return self.title

class SkillObj(models.Model):
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey()

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.skill.title