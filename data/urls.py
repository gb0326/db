from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('arrest/', views.arrest, name='arrest'),
    path('location/', views.location, name='location'),
    path('safemap/', views.safemap, name='safemap'),
    path('region/', views.region, name='region'),
    
]