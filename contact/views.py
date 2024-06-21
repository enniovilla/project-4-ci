from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    Renders the contact form page and handles form submission.
    If the request method is POST, validates and saves the ContactForm data.
    If the form is valid, a success message is displayed,
    and the user is redirected
    back to the contact page.
    If the form is invalid, an error message is displayed.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
