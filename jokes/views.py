from django.shortcuts import render
from .models import JokesClass
# Create your views here.
from django.http import HttpResponse

import requests



def home(request):
    res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
    if res.status_code == requests.codes.ok:
        joke_1 = JokesClass(title = str(res.json()['joke']))
        joke_1.save()
    context = {
        'jokes' : JokesClass.objects.all()
    }
    print(context)
    return render(request, "jokes/home.html", context)


def about(request):
    return render(request, "jokes/about.html")
