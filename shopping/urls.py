from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('sync-cart/', views.sync_cart, name='sync_cart'),
]
