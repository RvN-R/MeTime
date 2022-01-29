from django.shortcuts import render

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
