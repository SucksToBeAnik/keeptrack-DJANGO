from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import CustomUserCreationForm

# Create your views here.

    

def home_page(request):
    form = CustomUserCreationForm()
    context = {
            'form':form,
        }
    if request.method == "POST" and request.POST.get("action") == "logout":
        logout(request)
        messages.info(request,'You were successfully logged out!')
        return redirect('login-page')

    
    return render(request,'account/home_page.html',context)


def login_page(request):
    try:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
    except:
        messages.error(request, 'Please try to login with valid information!')

    return render(request,'account/login_page.html')

def register_page(request):
    form = CustomUserCreationForm()
    if request.method == "POST": 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"User account was created!")
            login(request,user)
            return redirect('home-page')
        else:
            messages.error(request,'An error has occured during Registration. Please try again!')
    context = {
        'form':form,
    }

    return render(request,'account/register_page.html',context)
