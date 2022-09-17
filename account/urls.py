from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name='login-page'),
    path('register/',views.register_page,name='register-page'),
    path('my-account/<str:username>/',views.account_page,name='account-page'),
    path('my-account-update/<str:username>/',views.account_update_page,name='account-update-page'),
    path('message/<str:receiver>/',views.message_form_page,name='message-form-page'),
    path('inbox/',views.inbox_page,name='inbox-page'),
]