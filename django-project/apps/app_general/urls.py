# coding=utf-8
# django libs
from django.urls import path, include

# 3rd party libs
from rest_framework.routers import DefaultRouter

# custom import
from . import views

# Namespace for URLs in this users app
app_name = 'app_general'
router = DefaultRouter()
# router.register('', views.ViewSet)

urlpatterns = [
    path('', views.home, name='home'),  # Home page view
    path('about/', views.about, name='about'),  # About page view
    path('service/', views.service, name='service'),  # Contact page view
    path('contact/', views.contact, name='contact'),  # Contact page view
    path('api/', include(router.urls)),
]

# when user go to path /app_name/ it will show api root page (endpoints list)
urlpatterns += router.urls
