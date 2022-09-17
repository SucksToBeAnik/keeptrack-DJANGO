from .models import Note
from django import forms
from django.forms import ModelForm

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title','note_image','body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'note_image':forms.FileInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}), 
        }