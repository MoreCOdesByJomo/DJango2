from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logs/',views.logs,name='logs'),
]