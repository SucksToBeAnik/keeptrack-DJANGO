from django.db import models

# Create your models here.
from account.models import Profile


from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey()

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey()

    owner = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)