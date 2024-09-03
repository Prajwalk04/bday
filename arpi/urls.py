from . import views
from django.urls import path
from .views import *
urlpatterns = [
     path('', views.login_view, name='login/'),
    # path('register/', views.register_view, name='register'),
    path('mainpage/', views.login_view, name='home'), 
   
]