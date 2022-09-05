from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.skill_page,name='skill-page'),
    path('skill_form_page/',views.skill_form_page,name='skill-form-page'),
]