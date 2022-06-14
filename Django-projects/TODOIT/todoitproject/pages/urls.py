from django.urls import path 
from pages import views 


urlpatterns = [ 
    path('', views.index, name='index'), 
    path('edit', views.edit, name='edit'),
    path('random_users', views.hw_users, name='random_users'), 
]