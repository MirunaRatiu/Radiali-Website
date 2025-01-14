from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


def index(request):
    products =  Product.objects.all()
    return render(request,'index.html',{'products' : products})


def search_feature(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            name__icontains=query
        )
    else:
        products = Product.objects.all()
   
    context = {
        'products': products,
        'search_query': query
    }
    return render(request, 'index.html', context)






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


