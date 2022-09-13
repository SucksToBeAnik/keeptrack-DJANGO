from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='keeptrack/images/')
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    bio = models.TextField(max_length=2000,blank=True,null=True)
    email = models.EmailField(max_length=255,blank=True,null=True)
    portfolio_site = models.URLField(max_length=500,blank=True,null=True)
    facebook = models.URLField(max_length=2000,blank=True,null=True)
    linkedin = models.URLField(max_length=2000,blank=True,null=True)
    youtube = models.URLField(max_length=2000,blank=True,null=True)


    def __str__(self):
        return self.username



def createProfile(sender, instance, created, **kwargs):
    print("Created:",created)
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            first_name = user.first_name,
            last_name = user.last_name,
        )
post_save.connect(createProfile,sender=User)



@receiver(post_delete,sender=Profile)
def deleteUser(sender,instance,**kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

@receiver(post_save,sender=Profile)
def updateUser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.username = profile.username
        user.email = profile.email
        user.save()