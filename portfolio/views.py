from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import Project


def preload(request):
    return render(request, "preload.html")


def index(request):
    projects = Project.objects.all()
    return render(request, "portfolio/index.html", {"projects":projects})


def whoami(request):
    return render(request, "portfolio/whoami.html")
