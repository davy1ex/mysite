from django.shortcuts import render, redirect

from .models import Project
from .forms import FinalForm


def redirect_to_index(request):
    return redirect(index)

def preload(request):
    return render(request, "preload.html")


def index(request):
    projects = Project.objects.all()
    return render(request, "portfolio/index.html", {"projects":projects})


def whoami(request):
    return render(request, "portfolio/whoami.html")



def welcome(request):
    return render(request, "quest/welcome.html")


def leveltwo(request):
    return render(request, "quest/leveltwo.html")


def final(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FinalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.cleaned_data['login'].lower())
            print(form.cleaned_data['password'].lower())
            if form.cleaned_data['login'].lower() == "вячеслав" and form.cleaned_data['password'].lower() == "лукьянчиков":                
                return redirect(thanks)
            
            elif form.cleaned_data['login'].lower() == "алексей" and form.cleaned_data['password'].lower() == "давыдов":
                return redirect(nome)

            elif form.cleaned_data['login'].lower() == "наталья" and form.cleaned_data['password'].lower() == "вавилова":
                return redirect(noyou)
            
            else:
                return redirect(nono)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FinalForm()

    return render(request, "quest/final.html", {'form': form})

def thanks(request):
    return render(request, 'quest/thanks.html')


def noyou(request):
    return render(request, 'quest/no2.html')


def nome(request):
    return render(request, 'quest/no1.html')

def nono(request):
    return render(request, 'quest/nono.html')