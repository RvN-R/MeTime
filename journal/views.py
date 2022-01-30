from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Journal



def journal(request):
    """a view to journal homepage"""
    user = request.user
    print(user)
    posts = Journal.objects.all().filter(poster=user)
    print(posts)
    context = {
        "user": user,
        "posts": posts
        }
    return render(request, "journal/journal.html", context)

