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


# def category_products(request, category):
#     # Filter products by category (case-sensitive)
#     products = Product.objects.filter(category__iexact=category.strip())
    
#     # Format the category name (for example, "generatoare" => "Generatoare")
#     category_name = category.replace('-', ' ').title()
    
#     # Render the filtered products in the template
#     return render(request, 'index.html', {'products': products, 'category': category_name})


def category_products(request, category):
    # Adăugăm debugging pentru a verifica ce primim în URL
    print(f"Categoria primită din URL: {category}")
    
    # Filtrăm produsele după categorie, liniuțele vor rămâne așa cum sunt în baza de date
    products = Product.objects.filter(category__iexact=category.strip())  # Filtrăm după categoria din URL
    
    # Verificăm dacă există produse
    if not products:
        print("Nu sunt produse pentru această categorie.")
    
    # Formatează numele categoriei pentru a-l afișa corect pe pagină:
    # Înlocuim liniuțele cu spațiu și facem prima literă a fiecărui cuvânt mare
    category_name = category.replace('-', ' ').title()  # Înlocuim liniuțele cu spațiu și punem prima literă mare
    
    # Trimitem produsele și categoria la template
    return render(request, 'index.html', {'products': products, 'category': category_name})


# def cart_view(request):
#     selected_products_ids = request.GET.getlist('selectedProducts')
#     products = Product.objects.filter(id__in=selected_products_ids)
#     return render(request, 'cart.html', {'products': products})
