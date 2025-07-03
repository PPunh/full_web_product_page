# coding=utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django_ratelimit.decorators import ratelimit

#Model and Form
from .models import ProductsModel, ProductsCategory
from .forms import ProductsModelForm, ProductsCategoryModelForm

# home app products
def home(request):
    all_products = ProductsModel.objects.all().order_by('-product_id')
    template = 'app_products/home.html'
    context = {
        'title': 'All Products',
        'all_products':all_products
    }
    return render(request, template, context)

#Product Details
def product_details(request, product_id):
    one_product = get_object_or_404(ProductsModel, product_id=product_id)
    template = 'app_products/product_details.html'
    context = {
        'title':'Product Details',
        'one_product':one_product
    }
    return render(request, template, context)


#Category
@login_required
@ratelimit(key='header:X-Forwarded-For', rate=settings.RATE_LIMIT, block=True)
def category(request):
    category_form = ProductsCategoryModelForm()
    all_category = ProductsCategory.objects.all().order_by('-category_id')
    template = 'app_products/categorys.html'
    context = {
        'title': 'Categorys',
        'all_category':all_category,
        'category_form':category_form
    }
    return render(request, template, context)



# Add category
@login_required
@ratelimit(key='header:X-Forwarded-For', rate=settings.RATE_LIMIT, block=True)
def add_new_category(request):
    if request.method == 'POST':
        category_form = ProductsCategoryModelForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('app_products:categorys')
        else:
            print(f"Category Errors: {category_form.errors}")
            return render(request, 'app_products/categorys.html',{
                'title': 'Add new Category',
                'category_form':category_form
            })
    return render('app_products/categorys.html')



#Product_list views
@login_required
@ratelimit(key='header:X-Forwarded-For', rate=settings.RATE_LIMIT, block=True)
def product_list(request):
    form = ProductsModelForm()
    all_product = ProductsModel.objects.all().order_by('-product_id')
    return render(request, 'app_products/product_list.html', {
        'title': 'Product List',
        'form': form,
        'all_product':all_product,
    })

#Edit Product Uploaded
def edit_product_uploaded(request, product_id):
    product_instance = get_object_or_404(ProductsModel, product_id=product_id)
    if request.method == 'POST':
        form = ProductsModelForm(request.POST, request.FILES, instance = product_instance)
        if form.is_valid():
            form.save()
            return redirect('app_products:product_list')
        else:
            print(f"Edit This Product Erros: {form.errors}")
    else:
        form = ProductsModelForm(instance = product_instance)
    template = 'app_products/edit_product_uploaded.html'
    context = {
        'title':'Edit this product',
        'product_instance':product_instance,
        'edit_this_product':form
    }
    return render(request, template, context)


#Add New Product
@login_required
@ratelimit(key='header:X-Forwarded-For', rate=settings.RATE_LIMIT, block=True)
def add_new(request):
    if request.method == 'POST':
        form = ProductsModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_products:product_list')
        else:
            print(f"Errors: {form.errors}")
            return render(request, 'app_products/product_list.html', {
                'title': 'Product List',
                'form': form
            })
    return redirect('app_products:product_list')
