from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import Project, Answer
from .forms import ReportForm


def preload(request):
    return render(request, "preload.html")


def index(request):
    projects = Project.objects.all()
    return render(request, "portfolio/index.html", {"projects":projects})


def brunyrus(request):
    return render(request, "brunyrus.html")


def answer(request):
    return render(request, "answer.html")


def report(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.cleaned_data['textarea'])
            a = Answer(text=form.cleaned_data['textarea'])
            a.save()
            return HttpResponseRedirect('/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportForm(auto_id=False)

    return render(request, 'report.html', {'form': form})


def thanks(request):
    return render(request, "thanks.html")
