#map urls to view fcts
from django.urls import path
from . import views

urlpatterns=[
    path('hi/', views.say_hello)#returns a URL pattern obj
]