from .cart import Cart

# Create context processor so our cart can be available in all pages
def cart(request):
    # Return default data from our Cart
    return {'cart': Cart(request)}