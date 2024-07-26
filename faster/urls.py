from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('', index, name='index'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('privacy', privacy, name='privacy')
    
]