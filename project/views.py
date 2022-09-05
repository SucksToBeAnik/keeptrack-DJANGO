from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.

def home_page(request):
    return render(request,'project/home_page.html')


def project_page(request):
    queryset = Project.objects.all()
    return render(request,"project/project_page.html",{'queryset':queryset})
