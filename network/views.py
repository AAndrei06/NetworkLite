from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Post, Comment
from django.contrib.auth.decorators import login_required
import random



@login_required(login_url = "login")
def home(request):


	context = {

		'posts':Post.objects.all().order_by('-date_posted'),
		'recommended_users': random.sample(list(User.objects.all()),12),
		'title':'Acasă'
		}

	return render(request,'network/home.html',context)

@login_required(login_url = 'login')
def contact(request):
	context = {
	'title':'Contacte',
	}
	return render(request,'network/contact.html',context)

@login_required(login_url = 'login')
def about(request):
	return render(request,'network/about.html')

@login_required(login_url = 'login')
def like_post(request):

	post_id = request.GET.get("post_id")
	post = get_object_or_404(Post,post_id = post_id)

	if request.user not in post.likes.all():
		post.likes.add(request.user)
		post.save()
	else:
		post.likes.remove(request.user)
		post.save()

	return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url = 'login')
def profile(request,pk):
	user_object = User.objects.get(pk = pk)
	posts_by_user = Post.objects.filter(author = user_object).order_by("-date_posted")

	context = {
		'user_object':user_object,
		'posts_by_user':posts_by_user,
		'pk_user':pk,
		'title':user_object.username
	}
	return render(request,'network/profile.html',context)

@login_required(login_url = 'login')
def follow_user(request):
	id_user = request.GET.get("user_id")
	user_object = get_object_or_404(User,pk = id_user)
	if request.user not in user_object.profile.followers.all():
		user_object.profile.followers.add(request.user)
		user_object.profile.save()
	else:
		user_object.profile.followers.remove(request.user)
		user_object.profile.save()
	return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url = 'login')
def search_user(request):

	if request.method == 'POST':
		username_to_search = request.POST.get('user-input-search-text')

		user_results = User.objects.filter(username__icontains = username_to_search)

		context = {
		'users':user_results,
		}

		return render(request,'network/search.html',context)

	return render(request,'network/search.html')


@login_required(login_url = 'login')
def create_post(request):

	if request.method == 'POST':
		current_user = request.user

		content = request.POST.get('post-content-input')
		image = request.FILES.get('post-photo-input')

		new_post = Post.objects.create(author = current_user,content = content,image = image)
		current_user.profile.nr_of_posts += 1
		current_user.profile.save()
		new_post.save()
		return redirect("post_detail",id = new_post.post_id)

	return render(request,'network/create_post.html',{'title':'Creează postare'})


@login_required(login_url = 'login')
def comment(request,id):
	comments = Comment.objects.filter(post_id = id)
	post = Post.objects.get(post_id = id)
	context = {
		'comments':comments,
		'title':'Comentarii',
	}

	if request.method == 'POST':
		text = request.POST.get("comment-field-input")

		new_comment = Comment.objects.create(post_id = id,author = request.user,text = text)
		post.nr_of_comments += 1
		post.save()
		new_comment.save()

	return render(request,'network/comments.html',context)


@login_required(login_url = 'login')
def post_detail(request,id):
	post = get_object_or_404(Post,post_id = id)
	context = {
	'post':post,
	'title':'Detaliu',
	}
	return render(request,'network/detail_post.html',context)


@login_required(login_url = 'login')
def post_update(request,id):

	post = get_object_or_404(Post,post_id = id)
	if request.user == post.author:
		context = {
		'post':post,
		'title':'Editează'
		}

		if request.method == 'POST':
			content = request.POST.get("post-content-input")
			keep_photo = request.POST.getlist("keep-photo")

			if request.FILES.get("post-photo-input") is not None:
				image = request.FILES.get("post-photo-input")
			else:
				image = post.image
			
			if len(keep_photo) == 0:
				image = None

			post.image = image
			post.content = content
			post.save()

			return redirect("home")

		return render(request,'network/create_post.html',context)
	else:
		return render(request,'network/create_post.html')

@login_required(login_url = 'login')
def delete_comment(request,id):
	comment = get_object_or_404(Comment,author = request.user,comment_id = id)
	if request.user == comment.author:
		post = Post.objects.get(post_id = comment.post_id)
		post.nr_of_comments -= 1
		post.save()
		comment.delete()
	else:
		return redirect("home")
	return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url = 'login')
def edit_comment(request,id):
	comment = get_object_or_404(Comment,author = request.user,comment_id = id)
	if comment == None:
		redirect("home")
	if request.user == comment.author:
		comments = Comment.objects.filter(post_id = comment.post_id)
		context = {
		"comment_object":comment,
		"comments":comments,
		'title':'Editează'
		}

		if request.method == 'POST':
			new_text = request.POST.get('comment-field-input-edit')
			comment.text = new_text
			comment.save()
			return redirect("comment",id = comment.post_id)
		return render(request,'network/comments.html',context)
	return render(request,'network/comments.html')


@login_required(login_url = 'login')
def delete_post(request,id):
	post = get_object_or_404(Post,post_id = id)
	if request.user == post.author:
		context = {
		'post':post,
		'title':'Șterge',
		}
		if request.method == 'POST':

			comments = Comment.objects.filter(post_id = id)
			if comments is not None:
				for comment in comments:
					comment.delete()

			request.user.profile.nr_of_posts -= 1
			request.user.save()
			request.user.profile.save()
			post.delete()

			return redirect('home')
		return render(request,'network/confirm_delete.html',context)
	else:
		return redirect('post_detail',id = post.id)


@login_required(login_url = 'login')
def settings(request):

	if request.method == 'POST':

		current_user = request.user

		# User Setting
		username = request.POST.get('username-input-setting')
		email = request.POST.get('email-input-setting')

		#Profile Setting
		job = request.POST.get('job-input-setting')
		location = request.POST.get('location-input-setting')
		contact = request.POST.get('contact-input-setting')
		bio = request.POST.get('bio-text-info')

		image = request.FILES.get('profile-image')

		background_image = request.FILES.get('profile-background-image')

		if image is not None:
			current_user.profile.profileimage = request.FILES.get('profile-image')
		else:
			image = request.user.profile.profileimage


		if background_image is not None:
			current_user.profile.background_image = request.FILES.get('profile-background-image')
		else:
			background_image = request.user.profile.background_image


		current_user.profile.job = job
		current_user.profile.bio = bio
		current_user.profile.location = location
		current_user.profile.contact = contact

		current_user.profile.save()

		current_user.username = username
		current_user.email = email
		current_user.save()

		return redirect('settings')


	return render(request,'network/settings.html',{'title':'Setări'})


def password_verify_register(password):

	if len(password) < 8:
		return False
	if any(char.isdigit() for char in password) == False:
		return False
	if any(char.islower() for char in password) == False:
		return False

	return True


def register(request):

	if request.method == 'POST':
		# Get Data
		username = request.POST.get('username-input')
		email = request.POST.get('email-input')
		password = request.POST.get('password-input')
		password_verify = request.POST.get('password-input-verify')

		# Verify Inputs
		if len(username) < 3:
			messages.info(request,"Numele de utilizator prea scurt")
			return redirect("register")

		if len(email) < 5:
			messages.info(request,"Email prea scurt")
			return redirect("register")

		if password_verify_register(str(password)) == False:
			messages.info(request,"Parola este prea slabă")
			return redirect("register")

		if password == password_verify:

			if User.objects.filter(email = email).exists():
				messages.info(request,"Email deja luat")
				return redirect("register")

			elif User.objects.filter(username = username).exists():
				messages.info(request,"Nume de utilizator deja luat")
				return redirect("register")

			else:
				# Create User
				user = User.objects.create_user(username = username,email = email,password = password)
				user.save()

				# Create Profile
				user_object = User.objects.get(username = user.username)
				profile = Profile.objects.create(user = user_object,id_user = user_object.id)
				profile.save()

				# Log In
				user = auth.authenticate(username = username,password = password)
				auth.login(request, user)

				return redirect("home")

		else:
			messages.info(request,"Parolele nu se potrivesc")
			return redirect('register')

	return render(request,'network/register.html')


def login(request):

	if request.method == 'POST':
		username = request.POST.get('username-input-login')
		password = request.POST.get('password-input-login')

		user = auth.authenticate(username = username,password = password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')

		messages.info(request,"Credentiale Invalide")
		return redirect('login')

	return render(request,"network/login.html")


@login_required(login_url = 'login')
def logout(request):
	auth.logout(request)
	return redirect('register')
