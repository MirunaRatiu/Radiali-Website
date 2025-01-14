# from django.shortcuts import render, get_object_or_404
# from productManagement.models import Product
# from django.http import JsonResponse
# import json

# def cart_view(request):
#     # Obține lista de produse din sesiune
#     cart = request.session.get('cart', [])
#     print("Cart content in session:", cart)  # Log pentru debug

#     # Selectează produsele din baza de date care există în coș
#     products = Product.objects.filter(name__in=cart)
#     return render(request, 'cart.html', {'products': products})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Cart
from productManagement.models import Product
from django.core.mail import send_mail

@login_required
def process_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    # Create email content
    order_details = "Your Order Details:\n\n"
    for item in cart_items:
        order_details += f"Product: {item.product.name}\n"
        order_details += f"Quantity: {item.quantity}\n"
        order_details += "-------------------------\n"
    
    # Send email
    send_mail(
        'Your Order Confirmation',
        order_details,
        'radu.sburlea33p2@gmail.com',
        ['mirunaratiu03@gmail.com', 'radu.sburlea33p2@gmail.com'],
        fail_silently=False,
    )
    
    # Clear cart after order
    cart_items.delete()
    
    messages.success(request, "Order processed! Check your email for confirmation.")
    return redirect('shopping:cart_detail')



@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        
        if quantity <= 0:
            messages.error(request, "Quantity must be at least 1.")
            return redirect("shopping:cart_detail")
        
        if product.stock < quantity:
            messages.error(request, "Not enough stock available.")
            return redirect("shopping:cart_detail")
        
        cart_item = Cart.objects.filter(user=request.user, product=product).first()
        
        if cart_item:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=quantity)
        
        # Update product stock
        product.stock -= quantity
        product.save()
        
        messages.success(request, f"{quantity} x {product.name} added to your cart.")
    else:
        messages.error(request, "Invalid request method.")
    
    return redirect("shopping:cart_detail")

@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_data = [{
        "product": item.product,
        "quantity": item.quantity
    } for item in cart_items]
    cart_count = Cart.objects.filter(user=request.user).aggregate(total=Sum('quantity'))['total'] or 0

    print("Cart items for user:", request.user, list(cart_items))

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "cart_count": cart_count,
    })

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    product = cart_item.product
    
    # Restore stock
    product.stock += cart_item.quantity
    product.save()
    
    cart_item.delete()
    messages.success(request, f"{product.name} removed from cart.")
    
    return redirect("shopping:cart_detail")

@login_required
def decrease_quantity(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    product = cart_item.product
    
    if cart_item.quantity <= 0:
        return redirect("shopping:cart_detail")
    product.stock += 1
    product.save()
    cart_item.quantity -= 1
    if cart_item.quantity == 0:
        cart_item.delete()
    else:
        cart_item.save()
    messages.success(request, f"{product.name}'s quantity decreased.")
    return redirect("shopping:cart_detail")

@login_required
def increase_quantity(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    product = cart_item.product
    
    # Restore stock
    if product.stock <= 0:
        messages.error(request, "Product is out of stock.")
        return redirect("shopping:cart_detail")
    product.stock -= 1
    product.save()
    cart_item.quantity += 1
    cart_item.save()
    messages.success(request, f"{product.name}'s quantity increased.")
    return redirect("shopping:cart_detail")