"""mailservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import th e include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os 
import smtplib
from email.message import EmailMessage
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import ssl
def home(request):
    print(request.POST)
    email=request.POST.get('email')
    #print(name)
    email_sender = "reraar1.1@gmail.com"
    email_password = "fixmwazidjzcxejr"
    email_reciever = email
    subject = "thanks for regestering"
    body = " thanks for regestering in my website thanks for the regestration"
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_reciever
    em['subject']=subject
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciever,em.as_string())
        print("email sent successfully")
    return HttpResponse("<h1>hello world</h1>")




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
]
