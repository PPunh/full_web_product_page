# coding=utf-8
# django libs
from django.urls import path, include

# 3rd party libs
from rest_framework.routers import DefaultRouter

# custom import
from . import views

# Namespace for URLs in this users app
app_name = 'app_products'
router = DefaultRouter()
# router.register('', views.ViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    path('categorys/', views.category, name='categorys'),
    path('add_new_category/', views.add_new_category, name='add_new_category'),
    path('product_list/', views.product_list, name='product_list'),  # Product list view
    path('product_list/edit_this_product/<int:product_id>/', views.edit_product_uploaded, name='edit_this_product'),
    path('add_new/', views.add_new, name='add_new'),
    path('api/', include(router.urls)),
]

# when user go to path /app_name/ it will show api root page (endpoints list)
urlpatterns += router.urls
