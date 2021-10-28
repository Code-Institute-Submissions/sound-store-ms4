from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


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


def messages_list(request):
    """Adin only page for showing contact messages"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    template = 'contact/message-list.html'

    message = Contact.objects.all()

    context = {
        'message': message,
    }
    return render(request, template, context)


def delete_message(request, contact_id):
    """Delete a message if superuser"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    messages.success(request, 'Message deleted')
    return redirect(reverse('messages_list'))

