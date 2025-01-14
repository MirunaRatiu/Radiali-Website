#map urls to view fcts
from django.urls import path
from . import views

# urlpatterns=[
#     path('products/', views.index),
    

# ]


urlpatterns = [
    # Add a dynamic URL for the category page
    path('produse/<str:category>/', views.category_products, name='category_products'),
    path('products/', views.index),  # URL pentru coșul de cumpărături,
    path('search/', views.search_feature, name='search_feature'),
    #path('search-suggestions/', views.search_suggestions, name='search_suggestions'),

]
