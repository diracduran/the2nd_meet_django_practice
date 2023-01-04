from django.urls import path
from demoapi import views


urlpatterns = [
    path('hello_world/', views.hello_world)
]
