from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import CustomUserCreationForm,ProfileForm,MessageForm
from note.models import FeaturedNote
from .models import Profile , Inbox, Message
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


def search_page(request,searched_value):
    try:
        queryset = Profile.objects.filter(username = searched_value)
    except:
        queryset = None
    context = {
        'queryset':queryset,
    }
    return render(request,'account/search_page.html',context)


# Create your views here.
@login_required(login_url='login-page')
def inbox_page(request):
    profile = request.user.profile
    inbox = profile.inbox
    received_messages = inbox.message_set.all()
    received_messages_count = inbox.message_set.count()

    sent_messages = profile.message_set.all()
    sent_messages_count = profile.message_set.count()

    context = {
        'received_messages':received_messages,
        'sent_messages':sent_messages,
        'r_count':received_messages_count,
        's_count':sent_messages_count,

    }
    return render(request,'account/inbox_page.html',context)

@login_required(login_url='login-page')
def message_form_page(request,receiver):
    form = MessageForm()
    receiver_profile = Profile.objects.get(username=receiver)
    receiver_inbox = Inbox.objects.get(owner = receiver_profile)
    if request.method == 'POST' and receiver_profile != request.user.profile :
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.inbox = receiver_inbox
            message.sender = request.user.profile
            message.save()
            messages.success(request, f'Message was sent to {receiver_profile}')
            return redirect('inbox-page')
    context = {
        'form':form,
        'receiver':receiver_profile,
    }
    return render(request,'account/message_form_page.html',context)

@login_required(login_url='login-page')
def account_update_page(request,username):
    print("hello")
    profile = Profile.objects.get(username=username)
    form = ProfileForm(instance=profile)    
    if request.method == 'POST':
        print("hello1")
        if  request.user.profile == profile:
            print("hello2")
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                print("hello3")
                profile = form.save(commit=False)
                profile.username = profile.username.lower()
                profile.save()
                return redirect('account-page',username=profile.username)
        else:
            messages.warning(request, 'You are not authorized to perform this task.')
            return redirect('home-page')

    
    context ={
        'form':form,
        'profile':profile,

    }
    return render(request,'account/account_update_page.html',context)

@login_required(login_url='login-page')
def account_page(request,username):
    profile = Profile.objects.get(username=username)

    my_projects = profile.project_set.all()
    project_count = profile.project_set.count()

    
    skill_count = profile.skill_set.count()

    featured_notes = FeaturedNote.objects.all()
    my_notes =[]

    for i in featured_notes:
        if i.note.owner == profile:
            my_notes.append(i)

    
    note_count = profile.note_set.count()
    context = {
        'profile':profile,
        'my_projects':list(my_projects),

        'project_count':project_count,
        'skill_count':skill_count,

        'my_notes':my_notes,
        'note_count':note_count,
    }

    return render(request,'account/account_page.html',context)



def home_page(request):
    latest_queryset = FeaturedNote.objects.select_related('note').order_by('-created_at')[:31]
    popular_queryset = FeaturedNote.objects.select_related('note').annotate(like_count=Count('note__like')).order_by('-like_count')[:21]
    context = {
            'latest_queryset':list(latest_queryset),
            'popular_queryset':list(popular_queryset),
        }
    if request.method == "POST" and request.POST.get("action") == "logout":
        logout(request)
        messages.info(request,'You were successfully logged out!')
        return redirect('login-page')
    elif request.method == 'POST' and request.POST.get('action') == 'notification-delete':
        profile = request.user.profile
        for notification in profile.notification_set.all():
            notification.delete()
        return redirect('home-page')
    elif request.method == 'POST' and request.POST.get('searched'):
        searched_value = request.POST.get('searched')
        return redirect('search-page', searched_value = searched_value)

    
    return render(request,'account/home_page.html',context)


def login_page(request):
    # try:
    #     username = request.POST.get("username").lower()
    #     password = request.POST.get("password")
    #     user = authenticate(request,username=username,password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home-page')
    # except:
    #     messages.error(request, 'Please try to login with valid information!')
    #     return render(request,'account/login_page.html')
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method=='POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request,"User does not exist. Please add proper details and try again.")
            return redirect('login-page')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, f"Welcome back {username}! Hope you are having a wonderful day!")
            return redirect(request.GET['next'] if 'next' in request.GET else 'home-page')
        else:
            messages.warning(request,"Your password is incorrect")

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
            return redirect('account-page',username=user.username)
        else:
            messages.warning(request,'An error has occured during Registration. Please try again!')
    context = {
        'form':form,
    }

    return render(request,'account/register_page.html',context)
