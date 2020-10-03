from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Userinfo
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import View
#from .forms import Userform
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        post = Userinfo()
        post.fname = request.POST.get('fname')
        post.lname = request.POST.get('lname')
        post.address = request.POST.get('address')
        post.city = request.POST.get('city')
        post.state = request.POST.get('state')
        post.zipcode = request.POST.get('zip_code')
        post.dob = request.POST.get('date of birth')
        post.phone = request.POST.get('phone number')
        post.email = request.POST.get('email')
        post.save()
        return render(request, 'register.html')  # will go to login page

    else:
        return render(request, 'register.html')

def signup_(request):

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def login_(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse("logged in")
        else:
            return render(request, 'login.html', context={'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', context={'form': form})


def index(request):
    return HttpResponse("Users Homepage")

