from photos.forms import *
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings



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



    return render(request, 'photos/about.html', context)

@login_required()
def comment(request,id):
	
	post = get_object_or_404(image,id=id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.image = post
			comment.save()
			return redirect('photos/home.html')
	else:
		form = CommentForm()

	return render(request,'comments.html',{"form":form})  

