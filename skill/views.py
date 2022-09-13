from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import F

from .models import Skill
from .forms import SkillForm
from django.contrib import messages

# Create your views here.


def single_skill_page(request,pk):
    skill = Skill.objects.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST' and request.POST.get("action") == "delete":
        skill.delete()
        messages.success(request, f"Your skill on {skill.title} has been successfully deleted!")
        return redirect('skill-page')
    elif request.method == 'POST' and request.POST.get("action") == "update":
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            return redirect('single-skill-page',pk=skill.id)
    context = {
        'skill':skill,
        'form':form,
    }
    return render(request,'skill/single_skill_page.html',context)


def skill_form_page(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
            messages.success(request,'A new skill has been successfully added!')
            return redirect('skill-page')
        else:
            messages.error(request,'An error has occured. Please try again.')
            return redirect('skill-form-page')
    context = {
        'form':form,
    }
    return render(request,'skill/skill_form_page.html',context)


def skill_page(request):
    profile = request.user.profile
    
    queryset =profile.skill_set.all()

    context = {
        'queryset':queryset,
    }
    return render(request,'skill/skill_page.html',context)