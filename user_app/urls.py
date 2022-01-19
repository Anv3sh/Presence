from django.urls import path,include
from .views import loginpage

urlpatterns=[
    path("",loginpage,name='login'),
]