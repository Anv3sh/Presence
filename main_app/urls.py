from django.urls import path
from .views import mainapp

urlpatterns=[
    path("main/",mainapp,name='main-app'),
]
