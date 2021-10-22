from django.shortcuts import render

def view_bag(request):
    """View which will show selected items on a shopping cart page"""
    return render(request, 'cart/cart.html')