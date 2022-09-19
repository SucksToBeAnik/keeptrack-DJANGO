from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from skill.models import Skill, SkillObj

# Create your views here.



@login_required(login_url='login-page')
def project_form_page(request):
    if request.GET.get('page') == 'create':
        profile = request.user.profile
        skill_queryset = profile.skill_set.all()
        form = ProjectForm()
        context ={
        'form':form,
        'page':'create',
        'skill_queryset':list(skill_queryset),
    }
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            skill_list = request.POST.getlist("skills")
            if form.is_valid() and skill_list:
                project = form.save(commit=False)
                project.owner = request.user.profile
                if request.POST.get('state') == '1':
                    project.project_state = True
                else:
                    project.project_state = False
                project.save()
                for skill_id in skill_list:
                    skill_obj = Skill.objects.get(pk=int(skill_id))
                    SkillObj.objects.create(skill=skill_obj,content_object=project)
                    skill_obj.update_skill_level(request,50)
                messages.success(request,f'Your project {project.title} has been added successfully!')
                return redirect('project-page')
            else:
                messages.warning(request, 'Please add some skills to your project.')
                return render(request,'project/project_form_page.html',context)
                
    elif request.GET.get('page') == 'update':
        id = request.GET.get('id')
        project = Project.objects.get(id = id)
        form = ProjectForm(instance=project)
        context ={
        'form':form,
        'page':'update',
        'skill_queryset':None,
    }
        if request.method == 'POST':
            form = ProjectForm(request.POST,request.FILES,instance=project)
            if form.is_valid():
                if request.POST.get('state') == '1':
                    project.project_state = True
                else:
                    project.project_state = False
                form.save()
                messages.success(request,f'Your project {project.title} has been updated successfully!')
                return redirect('single-project-page',pk=project.id)
                
    return render(request, 'project/project_form_page.html',context)

@login_required(login_url='login-page')
def single_project_page(request,pk):
    project = Project.objects.get(pk=pk)
    
    if request.method == 'POST' and project.owner == request.user.profile:
        project.delete()
        messages.success(request, f"Your project {project.title} has been deleted.")
        return redirect('project-page')
    context = {
        'project':project,
    }
    return render(request,'project/single_project_page.html',context)



@login_required(login_url='login-page')
def project_page(request):
    profile = request.user.profile
    queryset = profile.project_set.all()
    context = {
        'queryset':list(queryset),
    }
    return render(request,"project/project_page.html",context)
