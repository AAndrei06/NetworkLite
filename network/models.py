from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	id_user = models.IntegerField()
	contact = models.CharField(blank = True,max_length = 40,null=True)
	job = models.CharField(blank = True,max_length = 40,null = True)
	bio = models.TextField(blank = True,null=True)
	profileimage = models.ImageField(upload_to = "profile_images", default = "user_default.png")
	background_image = models.ImageField(upload_to = "profile_images",default = "photos/mountains.png")
	location = models.CharField(max_length = 100,null = True,blank = True)
	nr_of_posts = models.IntegerField(default = 0)
	followers = models.ManyToManyField(User,related_name = "follower",blank = True)

	def __str__(self):
		return self.user.username

	'''
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.profileimage.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.profileimage.path)
	'''
	def number_of_followers(self):
		return self.followers.count()


class Post(models.Model):
	post_id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
	author = models.ForeignKey(User,on_delete = models.CASCADE)
	content = models.TextField(blank = True)
	image = models.ImageField(upload_to = "post_images",blank = True)
	date_posted = models.DateTimeField(default = timezone.now)
	nr_of_comments = models.IntegerField(default = 0)
	likes = models.ManyToManyField(User,related_name = "post_like",blank = True)

	def __str__(self):
		return self.author.username

	def number_of_likes(self):
		return self.likes.count()


class Comment(models.Model):
	comment_id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
	post_id = models.CharField(max_length = 500)
	author = models.ForeignKey(User,on_delete = models.CASCADE)
	text = models.TextField(max_length = 400, blank = True)

	def __str__(self):
		return f"{self.author}"




