from django.shortcuts import render
import requests
from django.contrib.auth.models import User
# Create your views here.

def mainapp(request):
    user=User()
    name=user.username
    context={'names':name}

    return render(request,"main_app/main.html",context)
