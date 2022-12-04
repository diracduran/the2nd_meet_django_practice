from django.urls import path
from users import views


urlpatterns = [
    path('participant', views.participant, name='participant'),
    path('search/', views.search_participant, name='search_participant'),
    path('search/download_csv', views.download_csv, name='download_csv'),
]