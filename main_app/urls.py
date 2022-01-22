from django.urls import path
from .views import mainapp, webcam

urlpatterns=[
    path("main/",mainapp,name='main-app'),
    path("checkcamera/",webcam,name='check'),

    
]
