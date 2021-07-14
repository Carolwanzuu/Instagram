from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
     image = models.ImageField(blank=True)
     name = models.CharField(max_length=100)
     image_caption = models.TextField(max_length=300)
     created_on = models.DateTimeField(auto_now_add=True)
     last_modified = models.DateTimeField(auto_now=True)
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     image_likes = models.IntegerField(null=True, default=0)

     def __str__(self):
         return self.name

class Comments(models.Model):
  comment = models.CharField(max_length=200, null=True, blank=True)
  pic = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Likes(models.Model):
  likes = models.BooleanField(default=False)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)