from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_details(request):
    # Get the cart
    cart = Cart(request)
    cart_products =  cart.get_prods
    quantities = cart.get_qty
    return render(request, 'cart_details.html', {"cart_products": cart_products, "quantities": quantities})

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get the product
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        # Lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to Session
        cart.add(product=product, quantity=product_quantity)

        # Get Cart Count
        cart_count = cart.__len__()

        # Return response
        response = JsonResponse({'count': cart_count})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get the product
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        # Update the cart
        cart.update(product=product_id, quantity=product_quantity)