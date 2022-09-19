from django.urls import path
from . import views

urlpatterns = [
    path('',views.note_page,name="note-page"),
    path('note-form/<pk>',views.note_form_page,name="note-form-page"),
    path('single-note/<pk>/<slug:slug_title>/',views.single_note_page,name="single-note-page"),
    path('note-form-update/<pk>',views.note_form_page_update,name="note-form-page-update"),
    path('bookmark-note/',views.bookmark_note_page,name="bookmark-note-page"),
]