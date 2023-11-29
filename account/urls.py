# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('register/', views.register, name='register'),
]
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
     path('logout/', auth_views.LogoutView.as_view(next_page='account:login'), name='logout')
]
