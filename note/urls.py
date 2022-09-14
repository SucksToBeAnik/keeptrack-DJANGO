from django.urls import path
from . import views

urlpatterns = [
    path('',views.note_page,name="note-page"),
]