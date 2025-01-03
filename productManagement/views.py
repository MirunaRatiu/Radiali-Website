from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, get_object_or_404

# products = [
#     {'name': 'Generatoare', 'image_url': 'https://i.postimg.cc/tRSBZ9dR/eu30-removebg-preview.png', 'slug': 'generatoare'},
#     {'name': 'Mai Compactor', 'image_url': 'https://ntc.cz/thumbcache/k5qaw0qw051g8wo2au9jtwmswl1eaqkh1flnhan3qqu31w2ot9s5slu-wjgmszxakwwyjtl3251fqj5i5dlagx-zltt0bjgzrflesdie.png', 'slug': 'mai-compactor'},
#     {'name': 'Placi Compactoare', 'image_url': 'https://ntc.cz/thumbcache/...', 'slug': 'placi-compactoare'},
#     # Verifică dacă toate produsele au un `slug`.
# ]
# Create your views here= fct(request)->response
# we can pull data from db/transform/send email
def index(request):
    products =  Product.objects.all()
    #return HttpResponse('Hello world new product');
    #map this view to an URL
    #when we get a request to that URL, this function will be called

    return render(request,'index.html',{'products' : products})
#template to return HTML to a client
#instead of returning an HttpResponse, we use render to render a template and 
#and return HTML markup tu a client


# def category_page(request, slug):
#     # Obține categoria folosind slug-ul
#     category = get_object_or_404(Category, slug=slug)
    
#     # Obține produsele care aparțin acelei categorii
#     products_cat = category.products.all()
    
#     # Returnează șablonul cu produsele și categoria
#     return render(request, 'productManagement/category_page.html', {'category': category, 'products': products_cat})
# def product_page(request, slug):
#     product = next((p for p in products if p['slug'] == slug), None)
#     if not product:
#         return render(request, '404.html', status=404)
#     return render(request, 'product_page.html', {'product': product})
