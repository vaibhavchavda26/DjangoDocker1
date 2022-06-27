"""DockerLogs1 URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from dockerlogs1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addUser',views.addUser,name='addUser'),
    path('addSomething',views.addSomething,name='addUser'),
    path('addNew/<someNumber>',views.addNew,name='addNew'),
    path('addNewError/<someNumber>',views.addNewError,name='addNewError'),
    path('register/', views.index, name='register'),
    path('register/register1', views.register1, name='register1'),
    
]