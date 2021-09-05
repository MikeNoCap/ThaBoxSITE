from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'home.html')


def download(request):
    return render(request, "download.html")


def contribute(request):
    return render(request, "contribute.html")