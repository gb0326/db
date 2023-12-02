from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('arrest/', views.arrest, name='arrest'),
    path('safemap/', views.safemap, name='safemap'),
    path('region/', views.region, name='region'),
    path('yongsan/', views.yongsan, name='yongsan'),
    path('gangnam/', views.gangnam, name='gangnam'),
    path('dongjak/', views.dongjak, name='dongjak'),
]