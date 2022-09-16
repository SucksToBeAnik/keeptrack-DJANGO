from django.urls import path
from . import views

urlpatterns = [
    path('',views.note_page,name="note-page"),
    path('note_form_page/<pk>',views.note_form_page,name="note-form-page"),
    path('single_note_page/<pk>',views.single_note_page,name="single-note-page"),
    path('note_form_page_update/<pk>',views.note_form_page_update,name="note-form-page-update"),
]