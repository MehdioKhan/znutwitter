from django.shortcuts import render,redirect
from django.http import request,HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .forms import SignupUserForm,FeedForm
from .models import Feed
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
    posts = Feed.objects.all().order_by('-date')
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.user = request.user
            feed.date = timezone.now()
            feed.save()
            return redirect('home')
    else:
        form = FeedForm()
    return render(request,'twitterapp/index.html',{'posts':posts,'form':form})

def signup(request):
    if not request.user.is_authenticated:
        error = ""
        if request.method == "POST":
            form = SignupUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                username = form.cleaned_data.get('username').lower()
                email = form.cleaned_data.get('email').lower()
                if(not username_is_exist(username) and not email_is_exist(email)):
                    raw_password = form.cleaned_data.get('password1')
                    user.save()
                    temp_user = authenticate(username=username,password=raw_password)
                    login(request,user)
                    return redirect('home')
                elif email_is_exist(email):
                    error = "e"
                elif username_is_exist(username):
                    error = "u"
                elif email_is_exist(email_is_exist()) and username_is_exist(username_is_exist()):
                    error = "eu"
        else:
            form = SignupUserForm()
        return render(request,'twitterapp/signup.html',{'form':form,'error':error})
    else:
        return redirect('home')

def user(request,username):
    return redirect('home')

@login_required
def profile(request,username):
    post = Feed.objects.filter(user__username=username).order_by('-date')
    if len(post) > 5:
        post = post[:6]
    return render(request,'twitterapp/profile.html',{'post':post})

def username_is_exist(username):
    if User.objects.filter(username=username.lower()).exists():
        return True
    return False

def email_is_exist(email):
    if User.objects.filter(email=email.lower()).exists():
        return True
    return False
