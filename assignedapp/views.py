from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def aboutus(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def logs(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())

# Create your views here.
