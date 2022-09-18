from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile,Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        labels = {
            'password1':'Enter your password',
            'password2':'Confirm password'
        }
        
        # widgets ={
        #     'username': forms.TextInput(attrs={'class':'form-control'}),
        #     'first_name': forms.TextInput(attrs={'class':'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class':'form-control'}),
        #     'email': forms.EmailInput(attrs={'class':'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class':'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        # }
    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image','username','first_name','last_name','bio','email','portfolio_site','facebook','linkedin','youtube')

        widgets ={
            'profile_image': forms.FileInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control','rows':'3',}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'portfolio_site': forms.URLInput(attrs={'class':'form-control'}),
            'facebook': forms.URLInput(attrs={'class':'form-control'}),
            'linkedin': forms.URLInput(attrs={'class':'form-control'}),
            'youtube': forms.URLInput(attrs={'class':'form-control'}),
        }

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('body',)
        labels = {
            'body':'',
        }

        widgets = {
            'body':forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Write your message here...'})
        }