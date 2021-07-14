from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
  def setUp(self):
    self.new_user = User(username = "layersony", email = "layersony@gmail.com",password = "layersony1234")
    self.new_user.save()

  def tearDown(self):
    Profile.objects.all().delete()
    User.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.new_user.profile, Profile))

  def test_searchProfile(self):
    search = 'mutunga'
    self.new_user2 = User(username = "mutunga", email = "mutunga@gmail.com",password = "mutunga1234")
    self.new_user2.save()
    image_search = Profile.searchProfile(search)
    self.assertTrue(len(image_search) == 1)

class TestPost(TestCase):
  def setUp(self):
    self.location.save()
    self.new_user = User(username = "favian")
    self.new_user.save()
    self.new_post = Post(picture='test.jpg',caption = 'favorite' , uploadedBy = self.new_user)
    self.new_post.save_picture()
  
  def tearDown(self):
    Post.objects.all().delete()
    User.objects.all().delete()
    Post.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.new_post, Post))

  def test_savePicture(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'new spot' , uploadedBy = self.new_user)
    self.new_post2.save_picture()
    self.assertEqual(len(Post.objects.all()),2)

  def test_deletePicture(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'great!' , uploadedBy = self.new_user)
    self.new_post2.save_picture()
    self.assertEqual(len(Post.objects.all()),2)
    Post.delete_picture(self.new_post2.id)
    self.assertEqual(len(Post.objects.all()),1)

  def test_update(self):
    self.new_post.save_picture()
    self.new_post.update_caption(self.new_post.id, 'spot on')
    updated_post = Post.objects.get(id=self.new_post.id)
    self.assertEqual(updated_post.caption, 'spot on')   
  
  def test_allpics(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'nice one' , uploadedBy = self.new_user)
    self.new_post2.save_picture()
    self.assertEqual(len(Post.all_pictures()), 2)

  def test_userPictures(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'my own' , uploadedBy = self.new_user)
    self.new_post2.save_picture()
    usrpic = Post.user_pictures(self.new_user.username)
    self.assertEqual(len(usrpic), 2)

class TestComment(TestCase):
  def setUp(self):
    self.location.save()
    self.new_user = User(username = "favian")
    self.new_user.save()
    self.new_post = Post(picture='test.jpg',caption = 'grandeur' , uploadedBy = self.new_user)
    self.new_post.save_picture()
    self.new_comment = Comments(comment = "great", pic = self.new_post, user=self.new_user)

  def tearDown(self):
    Post.objects.all().delete()
    User.objects.all().delete()
    Comments.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.new_comment, Comments))

  def test_saveComment(self):
    self.new_comment.save_comment()
    self.assertEqual(len(Comments.objects.all()), 1)

  def test_deleteComment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comments.objects.all()) > 0)
    Comments.delete_comment(self.new_comment.id)
    self.assertTrue(len(Comments.objects.all()) == 0)
