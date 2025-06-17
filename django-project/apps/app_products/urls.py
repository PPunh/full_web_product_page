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
    path('categorys/', views.category, name='categorys'),
    path('add_new_category/', views.add_new_category, name='add_new_category'),
    path('product_list/', views.product_list, name='product_list'),  # Product list view
    path('add_new/', views.add_new, name='add_new'),
    path('api/', include(router.urls)),
]

# when user go to path /app_name/ it will show api root page (endpoints list)
urlpatterns += router.urls
