from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Journal(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title