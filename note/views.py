from django.shortcuts import render, redirect

from .models import Note, FeaturedNote, BookmarkedNote
from .forms import NoteForm

from feedback.forms import CommentForm
from feedback.models import Like,Comment
from project.models import Project
from skill.models import Skill
from account.models import Profile
from notification.models import Notification


from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login-page')
def bookmark_note_page(request):
    profile = request.user.profile
    queryset = profile.bookmarkednote_set.all()
    if request.method == 'POST':
        id = int(request.POST.get('bookmarked_note_id'))
        bookmarked_note = BookmarkedNote.objects.get(pk=id)
        if bookmarked_note.owner == profile:
            bookmarked_note.delete()
            return redirect('bookmark-note-page')
        else:
            messages.warning(request, 'You are not allowed to perform this task!')
            return redirect('bookmark-note-page')
    context = {
        'queryset':queryset,
    }
    return render(request,'note/bookmark_note_page.html',context)


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
    current_owner = Profile.objects.get(pk=current_owner_id)

    if request.method == 'POST' and request.POST.get('action') == 'delete' and request.user.profile == note.owner:
        note.delete()
        messages.success(request, 'Your note was deleted!')
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
            Notification.objects.create(
                owner = note.owner,
                body = f"{current_owner} has liked your note '{note.title}.'"
            )
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
            Notification.objects.create(
                owner = note.owner,
                body = f"{current_owner} has commented on your note '{note.title}'."
            )
            return redirect('single-note-page',pk=note.id)
        else:
            messages.error(request, 'Please add something to your feedback.')
    
    elif request.method == 'POST' and request.POST.get('action')[:14] == 'comment-delete':
        comment_id = int(request.POST.get('action')[15:])
        comment = Comment.objects.get(pk=comment_id)
        if request.user.profile == note.owner or request.user.is_superuser or request.user.profile == comment.owner:
            comment.delete()
            return redirect('single-note-page',pk=note.id)
        else:
            messages.warning(request, 'You are not authorized to delete this.')
            return redirect('single-note-page',pk=note.id)
    elif request.method == 'POST' and request.POST.get('action') == 'bookmark':
        BookmarkedNote.objects.create(
            owner = current_owner,
            note = note
        )
        messages.success(request, 'Added to bookmarks.')
        return redirect('single-note-page',pk=note.id)


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


@login_required(login_url='login-page')
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
        elif owner.coin >= 50 and count == 0:
            FeaturedNote.objects.create(note=note)
            owner.reduce_coin(50)
            messages.success(request, 'Your note was featured. Now others can see your note on the home page.')
            return redirect('note-page')
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




