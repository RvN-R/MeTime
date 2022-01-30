from django import forms
from django.forms import ModelForm
from .models import Journal


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Journal
        exclude = ('poster',)