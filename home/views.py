from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def index(request):
    """a view to render homepage"""
    return render(request, "home/index.html")


def resources(request):
    """a view to render resources page"""
    return render(request, "home/resources.html")


def about(request):
    """a view to render aboutpage"""
    return render(request, "home/about.html")


def breath(request):
    """a view to render meditation page"""
    return render(request, "home/breath.html")

