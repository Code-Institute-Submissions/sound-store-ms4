from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """Renders the contact form"""
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us, we will reply shortly.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Contact form not submitted. Pease ensure \
                all fields are filled out correctly and please try again!')
    else:
        form = ContactForm()
            
    context = {
        'form': form,
    }
    
    return render(request, 'contact/contact.html', context)
