# from django.urls import path
# from . import views

# urlpatterns = [
#     path('cart/', views.cart_view, name='cart'),
#     path('sync-cart/', views.sync_cart, name='sync_cart'),
# ]

from django.urls import path
from . import views

app_name = "shopping"

urlpatterns = [
    path("cart/", views.cart_detail, name="cart_detail"),
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("decrease/<int:cart_item_id>/", views.decrease_quantity, name="decrease_quantity"),  
    path("increase/<int:cart_item_id>/", views.increase_quantity, name="increase_quantity"),  
]

