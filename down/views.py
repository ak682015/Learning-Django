from django.shortcuts import render, redirect
from .models import DownClass
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm

import requests


from pytube import YouTube
from django.contrib import messages


def home(request):

    path = "/home/arman/Desktop"
    #     'downs' : YouTube(url).streams.first().download(path)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            print("url",url)
            messages.success(request, f"Downloaded {url} ")
            context = {

                'downs' : YouTube(url ).streams.first().download(path)
            }

            return render(request, "down/home.html", context)

    else:
        form = ContactForm()
    return render(request, 'down/home.html', {'form': form})

def about(request):
    return render(request, "down/about.html")


