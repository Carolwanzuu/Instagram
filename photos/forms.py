from users.models import Profile
from django import forms
from django.contrib.auth.models import User
from .models import *

# class UserForm(forms.ModelForm):
#   class Meta:
#     model = User
#     fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
  
  class Meta:
    model = Profile
    exclude = ('username','count')
    fields = '__all__'

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comments
    exclude = ('pic', 'user')
    fields = '__all__'

class LikeForm(forms.ModelForm):
  class Meta:
    model = Likes
    exclude = ('post', 'user')
    fields = '__all__'