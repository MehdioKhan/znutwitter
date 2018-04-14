from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .forms import SignupUserForm,FeedForm,ProfileEditForm
from .models import Feed,Profile
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import global_settings
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
    return render(request,'twitterapp/index.html',{'posts':posts,'form':form,})


def signup(request):
    if not request.user.is_authenticated:
        error = ""
        if request.method == "POST":
            form = SignupUserForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                username = form.cleaned_data.get('username').lower()
                email = form.cleaned_data.get('email').lower()
                if(not username_is_exist(username) and not email_is_exist(email)):
                    raw_password = form.cleaned_data.get('password1')
                    form.save()
                    temp_user = authenticate(username=username, password=raw_password)
                    profile = Profile(picture=global_settings.MEDIA_ROOT+"pics/user.png",user=temp_user)
                    profile.save()
                    login(request,temp_user)
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


def profile(request,username):
    user = User.objects.get(username=username)
    profile = get_object_or_404(Profile,user=user)
    user = get_object_or_404(User,username=username)
    post = Feed.objects.filter(user=user).order_by('-date')
    if len(post)>10:
        post = post[:10]
    return render(request,'twitterapp/profile.html',{'post':post,'profile':profile})


@login_required
def setting(request):
    profile = get_object_or_404(Profile,user=User.objects.get(username=request.user))
    if request.method == "POST":
        form = ProfileEditForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            return redirect('profile',username=request.user.username)
    else:
        form = ProfileEditForm(instance=profile)
    return render(request,'twitterapp/setting.html',{'form':form})


def username_is_exist(username):
    if User.objects.filter(username=username.lower()).exists():
        return True
    return False


def email_is_exist(email):
    if User.objects.filter(email=email.lower()).exists():
        return True
    return False
