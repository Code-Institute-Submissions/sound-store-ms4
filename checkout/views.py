from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    # Ensures user cannot access checkout by typing /checkout in url
    if not bag:
        messages.error(request, "You haven't added anything to your cart just yet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jnj9oFI8Dx6Ogw3ktFaDieglZN7JGfe1a5nyBxpHVR5g6MGqbjm2Dk7NVLPIZQRxkoSWcpOKL8Oug7PVeeE2CjM00xwT3BGNl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
