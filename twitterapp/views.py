from django.shortcuts import render,redirect
from django.http import request
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .forms import SignupUserForm
def index(request):
    return render(request,'twitterapp/index.html',{})

def signup(request):
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

def username_is_exist(username):
    if User.objects.filter(username=username.lower()).exists():
        return True
    return False

def email_is_exist(email):
    if User.objects.filter(email=email.lower()).exists():
        return True
    return False
