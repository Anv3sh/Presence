from django.shortcuts import render
import requests
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.
def loginpage(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
    return render(request,"user_app/index.html")

def registerpage(request):
    if request.method=='POST':
        user=User()
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.username=request.POST['username']
        user.email=request.POST['username']
        user.password=request.POST['password']
        user.save()
    return render(request,'user_app/register.html')