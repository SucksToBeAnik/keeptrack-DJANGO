from django.shortcuts import render, redirect

from .models import Note
from .forms import NoteForm
from project.models import Project
from skill.models import Skill

from django.contrib import messages
# Create your views here.


def note_form_page_update(request,pk):
    note = Note.objects.get(pk=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST,request.FILES,instance = note)
        if form.is_valid():
            form.save()
            return redirect('single-note-page',pk=pk)
    context = {
        'form':form,
    }
    return render(request,'note/note_form_page_update.html',context)

def single_note_page(request,pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        note.delete()
        messages.success(request, 'Your note was successfully deleted!')
        return redirect('home-page')

    context = {
        'note':note,
    }
    return render(request, 'note/single_note_page.html',context)

def note_page(request):
    queryset = Note.objects.all()
    context = {
        'queryset' : list(queryset),
    }

    return render(request,'note/note_page.html')


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




