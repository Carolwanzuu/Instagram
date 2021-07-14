from users.views import profile
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
  profilePic = models.ImageField(null=True, blank=True, default='default.jng')
  fullName= models.CharField(max_length=255, null=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = HTMLField(null=True, blank=True)
  phoneNumber = models.IntegerField(null=True)
  count = models.IntegerField(default=0, null=True, blank=True)
  
  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
       if created:
         profile.objects.create(username=instance)
         
         @receiver(post_save, sender=User)
         def save_user_profile(sender, instance, **kwargs):
           instance.profile.save()
           
           def __str__(self):
             return self.name

class Post(models.Model):
     image = models.ImageField(blank=True)
     name = models.CharField(max_length=100)
     image_caption = models.TextField(max_length=300)
     created_on = models.DateTimeField(auto_now_add=True)
     last_modified = models.DateTimeField(auto_now=True)
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     image_likes = models.IntegerField(null=True, default=0)

class Comments(models.Model):
  comment = models.CharField(max_length=200, null=True, blank=True)
  pic = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Likes(models.Model):
  likes = models.BooleanField(default=False)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)