"""blogweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from .views import home, details, addcomments, prof, register_view

urlpatterns = [
    path('', home.as_view(),name="home"),
    path('article/<int:pk>', details.as_view(),name="detail"),
    path('article/<int:pk>/comment/', addcomments.as_view(),name="add_comments"),
    path('article/<int:pk>/profi', prof.as_view(),name="profileinfo"),
    path('register/',register_view ),
    #path('tag/<slug:tag_slug>',home.as_view(),name="hometag"),

]
