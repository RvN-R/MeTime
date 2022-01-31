from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Journal
from .forms import CreatePostForm



def journal(request):
    """a view to journal homepage"""
    # user variable returns the request
    # user posts returns all the journal posts matching the users credentials
    # form variable reutrns the CreatePostForm created in forms.py
    form = CreatePostForm()
    user = request.user
    # print(user)
    posts = Journal.objects.all().filter(poster=user)
    # print(posts)
    context = {
        "user": user,
        "posts": posts,
        "form": form
        }
    if request.method == "POST":
        post_form = CreatePostForm(request.POST)
        try:
            if post_form.is_valid:
                post=post_form.save(commit=False)
                post.poster = request.user
                post.save()
                message.success(request,'Journal Entry Successful')
        except Exception as e:
            messages.error(
                request, "Please fill out the form correct"
            )
    return render(request, "journal/journal.html", context)

