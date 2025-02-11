"""Wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from wordcount_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('count', views.count, name="count"),
    path('result', views.result, name="result"),
    path('test', views.test, name="test"),
    path('test1', views.test1, name="test1"),
    path('test2', views.test2, name="test2"),
]
