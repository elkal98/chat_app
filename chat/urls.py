from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'chat'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('room/', views.chat_room, name='chat_room'),
]
