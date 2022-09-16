from django.shortcuts import render, redirect

from .models import Note, FeaturedNote
from .forms import NoteForm

from feedback.forms import CommentForm
from feedback.models import Like,Comment
from project.models import Project
from skill.models import Skill
from account.models import Profile


from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login-page')
def note_form_page_update(request,pk):
    note = Note.objects.get(pk=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST' and request.user.profile == note.owner:
        form = NoteForm(request.POST,request.FILES,instance = note)
        if form.is_valid():
            form.save()
            return redirect('single-note-page',pk=pk)
    context = {
        'form':form,
    }
    return render(request,'note/note_form_page_update.html',context)

@login_required(login_url='login-page')
def single_note_page(request,pk):
    note = Note.objects.get(pk=pk)
    form = CommentForm()
    current_owner_id = request.user.profile.id

    if request.method == 'POST' and request.POST.get('action') == 'delete' and request.user.profile == note.owner:
        note.delete()
        messages.success(request, 'Your note was successfully deleted!')
        return redirect('home-page')
    elif request.method == 'POST' and request.POST.get('action') == 'like':
        likes = Like.objects.values()
        count = 0
        for object in likes:
            if current_owner_id == object.get('owner_id') and int(pk) == object.get('object_id'):
                count += 1
                break
        if count == 0:
            Like.objects.create(content_object = note, owner_id = current_owner_id)
            return redirect('single-note-page',pk=note.id)
    
    elif request.method == 'POST' and request.POST.get('action') == 'comment-create':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_object = note
            comment.owner_id = current_owner_id
            profile = Profile.objects.get(pk=current_owner_id)
            profile.add_coin(25)
            comment.save()
            return redirect('single-note-page',pk=note.id)
        else:
            messages.error(request, 'Please add something to your feedback.')

    


    like_count = note.like.count()
    comment_count = note.comment.count()
    comments = note.comment.all()
    context = {
        'note':note,
        'like_count':like_count,
        'comment_count':comment_count,
        'comments': list(comments),
        'form':form,
    }
    return render(request, 'note/single_note_page.html',context)

def note_page(request):
    owner = request.user.profile
    queryset = owner.note_set.all()
    if request.method == 'POST':
        note_id = int(request.POST.get('note-id'))
        note = Note.objects.get(pk=note_id)
        count = 0
        for featured_note in note.featured_notes.all():
            if featured_note.note.id == note.id:
                count+=1
                break
        if count == 1:
            messages.info(request, 'You have already featured this note.')
        elif owner.coin >= 25 and count == 0:
            FeaturedNote.objects.create(note=note)
            owner.reduce_coin(25)
        else:
            messages.warning(request, 'You do not have enough coins to feature this note. Earn coins by commenting on others featured note.')

    context = {
        'queryset' : list(queryset),
    }

    return render(request,'note/note_page.html',context)


@login_required(login_url='login-page')
def note_form_page(request,pk):
    form = NoteForm()
    if request.method == 'POST' and request.GET.get('object') == 'project':
        form = NoteForm(request.POST,request.FILES)
        project = Project.objects.get(pk=pk)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user.profile
            note.content_object = project
            note.save()
            return redirect('single-project-page',pk=pk)

    elif request.method == 'POST' and request.GET.get('object') == 'skill':
        form = NoteForm(request.POST,request.FILES)
        skill = Skill.objects.get(pk=pk)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user.profile
            note.content_object = skill
            note.save()
            skill.update_skill_level(request,25)
            return redirect('single-skill-page',pk=pk)
    context = {
        'form':form,
    }
    return render(request,'note/note_form_page.html',context)




