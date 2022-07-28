from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact_us'),
    path('about-us/', views.about, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]