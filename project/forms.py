from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title','project_image','description','live_link','code_link')

        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'KeepTrack'}),
            'project_image':forms.FileInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'This web app tracks your skill'}),
            'live_link':forms.URLInput(attrs={'class':'form-control','placeholder':'Add a link to the live preiview of the project'}),
            'code_link':forms.URLInput(attrs={'class':'form-control','placeholder':'Add a link the code of the project'}),
        }