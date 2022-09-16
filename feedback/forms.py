from .models import Comment
from django import forms
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body':"",
        }

        widgets = {
            'body':forms.Textarea(attrs={'class':'form-control','rows':'3','placeholder':'Write your feedback here'})
        }