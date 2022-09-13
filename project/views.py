from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# def project_delete_page(request,pk):
#     project = Project.objects.get(id=pk)
#     delete = True
#     if request.method == 'POST':
#         project.delete()
#         messages.success(request,'The project has been deleted successfully!')
#         return redirect('project-page')
#     return render(request,'project/single_project_page.html',{'delete':delete})


@login_required(login_url='home-page')
def project_form_page(request):
    if request.GET.get('page') == 'create':
        form = ProjectForm()
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.owner = request.user.profile
                project.save()
                messages.success(request,'The project has been added successfully!')
                return redirect('project-page')
                
    elif request.GET.get('page') == 'update':
        id = request.GET.get('id')
        project = Project.objects.get(id = id)
        form = ProjectForm(instance=project)
        if request.method == 'POST':
            form = ProjectForm(request.POST,request.FILES,instance=project)
            if form.is_valid():
                if request.POST.get('state') == '1':
                    project.project_state = True
                else:
                    project.project_state = False
                form.save()
                messages.success(request,'The project has been updated successfully!')
                return redirect('single-project-page',pk=project.id)
                
    context ={
        'form':form,
    }


    return render(request, 'project/project_form_page.html',context)

@login_required(login_url='home-page')
def single_project_page(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, f"Project {project.title} has been deleted successfully!")
        return redirect('project-page')
    context = {
        'project':project,
    }
    return render(request,'project/single_project_page.html',context)


# def home_page(request):
#     return render(request,'project/home_page.html')
@login_required(login_url='home-page')
def project_page(request):
    profile = request.user.profile
    queryset = profile.project_set.all()
    context = {
        'queryset':list(queryset),
    }
    return render(request,"project/project_page.html",context)
