from django.shortcuts import render
from productManagement.models import Product
from django.http import JsonResponse
import json

def cart_view(request):
    cart = request.session.get('cart', [])  # Obține lista de produse din sesiune
    print("Cart content in session:", cart)  # Adaugă un log pentru debug
    products = Product.objects.filter(id__in=cart)  # Selectează produsele din baza de date
    return render(request, 'cart.html', {'products': products})
def sync_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = str(data.get('product_id'))
        action = data.get('action')

        print(f"Received Product ID: {product_id}, Action: {action}")  # Log pentru verificarea datelor primite

        cart = request.session.get('cart', [])

        if action == 'add' and product_id not in cart:
            cart.append(product_id)
        elif action == 'remove' and product_id in cart:
            cart.remove(product_id)

        # Actualizează sesiunea și marchează ca modificată
        request.session['cart'] = cart
        request.session.modified = True

        print(f"Updated cart in session: {request.session['cart']}")  # Log după actualizare

        return JsonResponse({'cart_count': len(cart)})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
