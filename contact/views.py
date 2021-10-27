from django.shortcuts import render


def contact(request):
    """Renders the contact form"""
    return render(request, 'contact/contact.html')
