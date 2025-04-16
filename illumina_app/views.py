from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def something(request):
    return HttpResponse("Suppp")


def home(request):
    return render(request, "main.html")