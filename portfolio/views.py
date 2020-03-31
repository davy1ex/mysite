from django.shortcuts import render, redirect

from .models import Project


def redirect_to_index(request):
    return redirect(index)

def preload(request):
    return render(request, "preload.html")


def index(request):
    projects = Project.objects.all()
    return render(request, "portfolio/index.html", {"projects":projects})


def whoami(request):
    return render(request, "portfolio/whoami.html")
