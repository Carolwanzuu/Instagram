from django.shortcuts import render
from .models import *



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'photos/home.html', context)

def about(request):
    return render(request, 'photos/about.html')