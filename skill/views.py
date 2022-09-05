from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Skill
from .forms import SkillForm
from django.contrib import messages

# Create your views here.



def skill_form_page(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
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
    queryset = Skill.objects.all()

    context = {
        'queryset':queryset,
    }
    return render(request,'skill/skill_page.html',context)