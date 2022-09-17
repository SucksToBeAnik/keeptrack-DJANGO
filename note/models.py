from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from account.models import Profile
from feedback.models import Like, Comment

# Create your models here.


class Note(models.Model):
    comment = GenericRelation(Comment)
    like = GenericRelation(Like)


    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)
    object_id = models.IntegerField()
    content_object = GenericForeignKey()

    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    note_image = models.ImageField(null=True, blank =True, upload_to='keeptrack/images/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class FeaturedNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE,related_name="featured_notes")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

class BookmarkedNote(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']