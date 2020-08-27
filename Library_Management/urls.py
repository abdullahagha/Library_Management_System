"""Library_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name='home'),
    path('addbook/',Add_book, name='addbook'),
    path('viewbook/',viewbook, name='viewbook'),
    path('returnbook/(?P<pid>[0-9]+)',returnbook,name='returnbook'),
    path('issuebook/',Issue_Book, name='issuebook'),
    path('Adminlogin/', Adminlogin, name='loginadmin'),
    path('signupstudent/',Signup_student, name='signupstudent'),
    path('registerstudent/',Registerstudent, name='registerstudent'),
    path('studentlogin/',Student_login, name='studentlogin'),
    path('vieworder/',ViewOrder, name='vieworder'),
    path('viewissue/',Viewissue, name='viewissue'),
    path('viewprofile/(?P<pid>[0-9]+)',viewprofile, name='viewprofile'),
    path('fine/(?P<pid>[0-9]+)',Fine,name='fine'),
    path('editprofile/(?P<pid>[0-9]+)',edit,name='editprofile'),
    path('editstudent/(?P<pid>[0-9]+)',editstudent,name='editstudent'),
    path('editbook/(?P<pid>[0-9]+)',edit_book,name='editbook'),
    path('deletestudent/(?P<pid>[0-9]+)',deletestudent,name='deletestudent'),
    path('deletebook/(?P<pid>[0-9]+)',bookdelete,name='deletebook'),
    path('fine2/(?P<pid>[0-9]+)',Fine2,name='fine2'),
    path('logout/',Logout,name='logout'),
    path('viewstudent/',viewstudent, name='viewstudent'),
    path('viewItem/',viewItem, name='viewItem'),
    path('employees/',viewEmployee, name='employees'),
    path('authors/',viewAuthors, name='authors'),
    path('add_employee/',add_employee, name='add_employee'),
    path('deleteemployee/(?P<pid>[0-9]+)',deleteemployee,name='deleteemployee'),
    path('deleteauthor/(?P<pid>[0-9]+)',deleteauthor,name='deleteauthor'),

    path('editemployee/(?P<pid>[0-9]+)',editemployee,name='editemployee'),
    path('editauthor/(?P<pid>[0-9]+)',editauthor,name='editauthor'),



]

