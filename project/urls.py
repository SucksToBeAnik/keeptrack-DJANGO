from django.urls import path
from . import views

urlpatterns = [
    path('',views.project_page,name='project-page'),
    path('single_project/<str:pk>/',views.single_project_page,name='single-project-page'),
    path('create/',views.project_form_page,name='project-form-page-create'),
    path('update/',views.project_form_page,name='project-form-page-update'),
    # path('delete/<str:pk>',views.project_delete_page,name='project-delete-page'),
]