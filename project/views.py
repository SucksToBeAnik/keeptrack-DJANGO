from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.

def single_project_page(request,pk):
    project = Project.objects.get(id=pk)
    context = {
        'project':project,
    }
    return render(request,'project/single_project_page.html',context)


def home_page(request):
    return render(request,'project/home_page.html')

def project_page(request):
    queryset = Project.objects.all()
    context = {
        'queryset':list(queryset),
    }
    return render(request,"project/project_page.html",context)
