from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header ='Cargo Route Runner ADMIN'
admin.site.site_title ='Cargo Route Runner ADMIN PORTAL'
admin.site.index_title='WELCOME TO CARGO ROUTE RUNNER ADMIN PORTAL'


class SenderDetailsSite(admin.ModelAdmin):
    model = Sender   

    list_display =('user', 'name', 'country', 'status')

    list_filter = ['name', 'country',]

    search_fields = ['name', 'country',]
    
class ReceiverDetailsSite(admin.ModelAdmin):
    model = Reciever   

    list_display =('user', 'name','custom_id', 'country', 'status')

    list_filter = ['name','custom_id', 'country',]

    search_fields = ['name', 'custom_id', 'country',]




admin.site.register(Sender, SenderDetailsSite)
admin.site.register(Reciever, ReceiverDetailsSite)