from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import RegistrationForm, AccountAuthenticationForm, BlogPostForm
from django.contrib.auth import login, authenticate, logout
from .models import BlogPost
# Create your views here.
def home_view(request):

	blogs = BlogPost.objects.all()
	context ={"blogs": blogs}

	return render(request, 'home.html', context=context)


def signup_view(request):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.username))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(username=username, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'signup/signup.html', context)


def logout_view(request):
	logout(request)
	return redirect("home")


def login_view(request):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")


	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "login/login.html", context)


def contact(request):

	return render(request, "contact.html")

def about(request):

	return render(request, "about.html")

def post(request):
	user = request.user
	if request.POST:

		if user.is_authenticated: 

			form = BlogPostForm(request.POST, request.FILES)
			print(request.FILES)
			if form.is_valid():
				blog_post = form.save(commit=False)
				blog_post.user = user
				blog_post.save()

				return redirect('post')
			else:
				print(form.errors)
		else:
			form = BlogPostForm()
			return redirect('login')

	else:
		form = BlogPostForm()


	return render(request, 'post.html', {'form': form})