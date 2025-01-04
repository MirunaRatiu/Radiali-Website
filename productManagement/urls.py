#map urls to view fcts
from django.urls import path
from . import views

# urlpatterns=[
#     path('products/', views.index),
    

# ]


urlpatterns = [
    # Add a dynamic URL for the category page
    path('produse/<str:category>/', views.category_products, name='category_products'),
]
