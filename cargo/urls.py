from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('cargo_login', cargo_login , name='cargo_login'),
    path('cargo_register', cargo_register , name='cargo_register'),
    path('dashboard', dashboard, name='dashboard'),
    path("sent_shipment", sent_shipment, name='sent_shipment'),
    path("receiver_form", receiver_form, name='receiver_form'),
    path('tracking_shipment', tracking_shipment , name='tracking_shipment'),
    path('tracking', search, name='search'),
    path('tracking/<str:custom_id>', search_info, name='search_info'),
    path('receiving_shipment', receiving_shipment , name='receiving_shipment'),
    path('shipment_table', shipment_table, name='shipment_table')
    
    
]