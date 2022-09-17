from django.db import models

# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey

from account.models import Profile
# Create your models here.


class Notification(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)