from django import forms
from .models import Contact
from phonenumbers import is_valid_number, is_possible_number
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.exceptions import ValidationError

# Create your forms here.

PLACE_HOLDERS = {
    "Name": "What is your name?",
    "Email": "What is your email address?",
    "Address": "Property Address",
    "City": "Property city",
    "Phone Number": "Best number to reach you (ext-number)",
}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'Address': forms.Textarea(attrs={'rows': 8, 'cols': 40}),
            "Phone Number": PhoneNumberPrefixWidget()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['placeholder'] = field.label.title()
            field.widget.attrs['placeholder'] = PLACE_HOLDERS.get(field.label.title())
        self.fields["address"].widget.attrs.update(rows=4)
