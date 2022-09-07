from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blogs import views


urlpatterns = [
    path('', views.show_blog, name='show_blog'),
    path('blog/<slug:author>/<slug:slug>/view', views.single_blog, name='single_blog'),
]