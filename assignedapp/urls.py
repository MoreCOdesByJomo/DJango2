from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logs/',views.logs,name='logs'),
    path('addstudent',views.addstudent, name='addingstudent'),
    path('edittudent/<id>', views.editstudent, name='editstudent'),
    path('updatetudent/<id>', views.updatestudent, name='updatestudent'),
    path('deletetudent/<id>', views.deletestudent),
    path('/dashboard',views.dashboard,name='dashboard'),
]