from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """View which will show selected items on a shopping cart page"""
    return render(request, 'cart/cart.html')


def add_to_bag(request, item_id):
    """Add amount of a product to the shopping cart"""

    # Get specific product id
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # Check if there is a 'bag' variable stored in the session,
    # if not then make one
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'You have updated quantity \
            of {product.name} to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'You have added \
            {quantity} {product.name}(s) to your cart')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity in the bag to given amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated quantity of \
            {product.name} to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'You have removed \
            {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Removes item from bag"""

    bag = request.session.get('bag', {})

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'There was an error removing item {e}')
        return HttpResponse(status=500)
