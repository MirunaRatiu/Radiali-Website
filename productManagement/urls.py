#map urls to view fcts
from django.urls import path
from . import views

urlpatterns=[
    path('products/', views.index),
    # path('category/<slug:slug>/', views.category_page, name='category_page'),
    # path('product/<slug:slug>/', views.product_page, name='product_page'),

]