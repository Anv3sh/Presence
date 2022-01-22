from django.shortcuts import render
import requests
from django.contrib.auth.models import User
import cv2
import threading
from django.contrib.auth.decorators import login_required
# Create your views here.

def mainapp(request):
    pass

    return render(request,"main_app/dummy.html")

def webcam(request):
    camera = cv2.VideoCapture(0)
    while True:
        return_value,image = camera.read()
        cv2.imshow('image',image)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('/static/main_app/test.jpg',image)
            break
    camera.release()
    cv2.destroyAllWindows()


    return render(request,'main_app/main.html')
