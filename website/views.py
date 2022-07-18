from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.template import loader
from django.core.mail import send_mail, BadHeaderError
from .models import *
from .forms import ContactForm


# Create your views here.
def index(request):
    template = loader.get_template('website/index_1.html')

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
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'address': form.cleaned_data['address'],
                'city': form.cleaned_data['city'],
                'phone_number': form.cleaned_data['phone_number'],
            }
            # message = "\n".join(body.values())
            print(body.values())
            try:
                # send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
                print("XYZ")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse("Your query has been sent.", status=200)
            # return HttpResponse("Message sent successfully", status=200)
        else:
            print("Form invalid")
            print(form)
            return HttpResponse("Bad request", status=400)
    form = ContactForm()
    return render(request, 'website/index.html', {'form': form})
