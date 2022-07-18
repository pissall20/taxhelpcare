from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.template import loader
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