from django.shortcuts import render
from django.http import HttpResponse

from .models import Skill

# Create your views here.


def skill_page(request):
    queryset = Skill.objects.all()

    context = {
        'queryset':queryset,
    }
    return render(request,'skill/skill_page.html',context)