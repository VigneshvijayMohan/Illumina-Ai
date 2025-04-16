
from . import views

from django.urls import path

urlpatterns = [
    path("some/", views.something, name="some"),
    path('', views.home, name='home'),
    path('upload/', views.file_upload, name='file_upload'),
    path('chat/', views.chat_app, name='chat_app'),
    path('chat/message/', views.chat_view, name='chat_api'),
]
