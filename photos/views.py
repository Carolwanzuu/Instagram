from photos.forms import ProfileForm
from django.shortcuts import render
from .models import *



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'photos/home.html', context)

def about(request):
    if request.method == 'POST':
        a_form = ProfileForm(request.POST)

        if a_form.is_valid():
            a_form.save()
    else:
        a_form=ProfileForm()

    context = {
        'a_form': a_form
        }



    return render(request, 'photos/about.html', {})