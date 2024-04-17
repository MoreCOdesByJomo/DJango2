from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .models import Register

def home(request):
    template = loader.get_template('base.html')
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

@csrf_exempt
def addstudent(request):
    if request.method == 'POST':
        name = request.POST.get('govtname')
        age = request.POST.get('age')
        country = request.POST.get('cntry')

        member1=Register(name=name,age=age,country=country)
        member1.save()
        #fetch the member's data to be displayed
        """
        data = Register.objects.all():
        context = {'data': data}
        """
        return render(request,'dashboard.html')

# Create your views here.
