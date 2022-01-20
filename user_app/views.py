from django.shortcuts import render
import requests
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.
def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
    return render(request,"user_app/index.html")

