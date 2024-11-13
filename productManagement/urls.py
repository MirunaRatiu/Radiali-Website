#map urls to view fcts
from django.urls import path
from . import views

urlpatterns=[
    path('products/', views.index)#returns a URL pattern obj
]