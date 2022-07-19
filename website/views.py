from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


# Create your views here.
def index(request):
    template = loader.get_template('website/index.html')

    contact_form = ContactForm()
    context = {
        "contact_form": contact_form,
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Website Inquiry"
            print(form.cleaned_data)
            body = {
                'Name': form.cleaned_data['name'],
                'Email': form.cleaned_data['email'],
                'Address': form.cleaned_data['address'],
                'City': form.cleaned_data['city'],
                'Phone Number': str(form.cleaned_data['phone_number']),
            }
            email_header = "A new client is trying to contact you:"
            message = "\n".join([email_header] + [f"{key}: {value}" for key, value in body.items()])
            response = "Your message has been sent. Thank you!"
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                response = "Bad Header Sent"
                return HttpResponse(response)
            return HttpResponse(response, status=200)
        else:
            if "phone_number" in form.errors:
                response = 'Enter a valid phone number (e.g. (201) 555-0123) or a number with an international call prefix.'
            else:
                response = 'Oops! There was an issue. Please mail us at support@gmail.com'
            return HttpResponse(response, status=403)

    form = ContactForm()
    return render(request, 'website/index.html', {'form': form})
