
from . import views

from django.urls import path

urlpatterns = [
    path("some/", views.something),
    path("", views.home, name='home')
]
