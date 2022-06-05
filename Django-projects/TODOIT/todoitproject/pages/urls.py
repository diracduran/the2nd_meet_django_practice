from django.urls import path 
from pages import views 


urlpatterns = [ 
    path('', views.index, name='index'), 
    path('random_users', views.hw_users, name='random_users'), 
]