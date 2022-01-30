from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Journal



def journal(request):
    """a view to journal homepage"""
    posts = Journal.objects.all()
    user = str(request.user)
    context = {
        "posts": posts,
        "user": user
        }
    return render(request, "journal/journal.html", context)

