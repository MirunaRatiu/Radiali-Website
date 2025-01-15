from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Register route
    path('login/', views.login, name='login'),          # Login route
    #path('register/', views.register),  
    #path('login/', views.login),          
]
