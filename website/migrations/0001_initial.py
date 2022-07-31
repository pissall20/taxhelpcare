# Generated by Django 4.0.5 on 2022-07-31 14:12

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('address', models.TextField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('mortgage', models.CharField(max_length=10, null=True)),
                ('additional_liens', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
