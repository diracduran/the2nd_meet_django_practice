from django.urls import path
from excursions import views


urlpatterns = [
    path('excursions', views.excursions, name='excursions'),
]
