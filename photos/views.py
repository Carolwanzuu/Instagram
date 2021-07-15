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
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form=ProfileForm()
        
        


    return render(request, 'users/profile.html', {'form':form})

@login_required()
def comment(request,id):
	
	post = get_object_or_404(id=id)	
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

@login_required()
def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	 follower = Follow.objects.filter(user = profile)
	 return render(request, 'users/profile.html',{"current_user":current_user,"profile":profile,"follower":follower})

@login_required()
def timeline(request):
	current_user = request.user 
	F_profile = Profile.objects.order_by('-time_uploaded')
	comment = Comments.objects.order_by('-time_comment')
	

	return render(request, 'users/timeline.html',{"F_profile":F_profile,"comment":comment})

@login_required()
def like(request,post_id):
	post = image.objects.get(id=post_id)
	likes +=1
	save_like()
	return redirect(timeline)

def search_results(request):
    if 'pic' in request.GET and request.GET["pic"]:
        search_term = request.GET.get("pic")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search_pic.html',{"message":message,"pics": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_pic.html',{"message":message})


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profilePic = form.cleaned_data['profile_pic']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.u_name = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileForm()
    except:
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileForm()


    return render(request,'users/new_profile.html',{"title":title,"current_user":current_user,"form":form})