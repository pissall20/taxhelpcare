from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    mortgage = models.BooleanField(choices=((True, "Yes"), (False, "No")))
    additional_liens = models.BooleanField(choices=((True, "Yes"), (False, "No")))

    def __str__(self):
        return self.email
