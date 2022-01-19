from django.urls import path,include
from .views import loginpage, registerpage  

urlpatterns=[
    path("",loginpage,name='login'),
    path("register/",registerpage,name='register'),
]