from django.shortcuts import render, redirect

from .models import Note
# Create your views here.


def note_page(request):
    queryset = Note.objects.all()
    context = {
        'queryset' : list(queryset),
    }

    return render(request,'note/note_page.html')