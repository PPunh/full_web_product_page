# coding=utf-8
from django.shortcuts import render
from apps.app_products.models import ProductsModel

# HOme page view
def home(request):
    product_in_homepage = ProductsModel.objects.filter(product_show_in_homepage=True)[0:3]
    template = 'app_general/home.html'
    context = {
        'title': 'Home',
        'product_in_homepage':product_in_homepage
    }
    return render(request, template, context)


# About page view
def about(request):

    template = 'app_general/about.html'
    context = {
        'title': 'About',
    }
    return render(request, template, context)


# Service views 
def service(request):

    template = 'app_general/service.html'
    context = {
        'title': 'Our Services',
    }
    return render(request, template, context)


# Contact page view
def contact(request):
    
    template = 'app_general/contact.html'
    context = {
        'title': 'Contact Us',
    }
    return render(request, template, context)