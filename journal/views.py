from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def journal(request):
    """a view to journal homepage"""
    return render(request, "journal/journal.html")

