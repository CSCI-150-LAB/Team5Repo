from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("homepage")

def register (request):
    #return HttpResponse("register")
    return render(request, "Register.html")

def login (request):
    #return HttpResponse("login")
    return render(request, "login.html")