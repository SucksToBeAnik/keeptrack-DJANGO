from django import forms
from django.forms import ModelForm
from .models import Skill

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ('title','description','skill_type')

        labels = {
            'title':'Skill Title',
            'skill_type':'Skill Type'
        }

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Python'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Python is easy to learn...'}),
            'skill_type':forms.Select(attrs={'class':'form-control','placeholder':'Programming Language'}),
            
        }

        