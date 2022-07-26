import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.template import loader
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


# Create your views here.
def index(request):
    contact_form = ContactForm()
    context = {
        "contact_form": contact_form,
    }
    return render(request, 'website/index.html', context)


def about(request):
    context = {}
    return render(request, 'website/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Website Inquiry"
            print(form.cleaned_data)
            form.cleaned_data['mortgage'] = form.cleaned_data['mortgage'].lower()
            form.cleaned_data['additional_liens'] = form.cleaned_data['additional_liens'].lower()
            body = {
                'Name': form.cleaned_data['name'],
                'Email': form.cleaned_data['email'],
                'Address': form.cleaned_data['address'],
                'City': form.cleaned_data['city'],
                'Phone Number': str(form.cleaned_data['phone_number']),
                "Mortgage": form.cleaned_data['mortgage'],
                "Additional Liens": form.cleaned_data['additional_liens']
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
            response = {}
            if "phone_number" in form.errors:
                response['phone_number'] = 'Enter a valid phone number (e.g. (201) 555-0123) or a number with an international call prefix.'
            if "mortgage" in form.errors:
                response['mortage'] = 'Mortage: Please answer in yes/no'
            if "additional_liens" in form.errors:
                response['additional_liens'] = 'Additional Liens: Please answer in yes/no'
            return JsonResponse(response, status=403)
    else:
        form = ContactForm()
    return render(request, 'website/index.html', {'form': form})
