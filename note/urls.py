from django.urls import path
from . import views

urlpatterns = [
    path('',views.note_page,name="note-page"),
    path('note_form/<pk>',views.note_form_page,name="note-form-page"),
    path('single_note/<pk>',views.single_note_page,name="single-note-page"),
    path('note_form_update/<pk>',views.note_form_page_update,name="note-form-page-update"),
    path('bookmark_note/',views.bookmark_note_page,name="bookmark-note-page"),
]