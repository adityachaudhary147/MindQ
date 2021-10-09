from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from .decorators import unauthenticated_user
from user_profile.models import Profile
from django.contrib.auth.models import User

# Create your views here.


@unauthenticated_user
def signupPage(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already taken!')
                return redirect('signup')
            else:
                form.save()
                messages.success(request,'Your account has been successfully created')
                return redirect('login')
        else:
            messages.info(request,'Username already exists!')
            return redirect('signup')
    context = {
        'form' : CreateUserForm()
    }
    return render(request,'authentication/signup.html',context)


@unauthenticated_user
def loginPage(request):
    if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('questions')
            else :
                messages.error(request,'Username or password is incorrect')

    context = {}
    return render(request,'authentication/login.html',context)

@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('login')
