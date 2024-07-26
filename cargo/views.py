from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# import forms and models
from .forms import UserCreationForm, LoginForm, SenderForm, ReceiverForm, SearchForm
from django.http import HttpResponseRedirect 
from .functions import *
from .models import *

#404 handler
from django.shortcuts import render, get_object_or_404

#send mail and settings
from django.core.mail import send_mail
from django.conf import settings

#custom mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


# Create your views here.



# Login account
def cargo_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('dashboard')
    else:
        form = LoginForm()
    
    return render(request, 'cargo/login.html',{
        'form': form
    })
    
    


# Create user
def cargo_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo_login')
    else:
        form = UserCreationForm()
    
    return render(request, 'cargo/register.html', {
        'form': form
        })
    
    
    

# dashboard
@login_required(login_url='cargo_login')
def dashboard(request):
    sendings  = Sender.objects.all()
    Received ="Received"
    Moving = "On_the_move"
    return render(request, 'cargo/index.html',{
        "sendings" : sendings ,
        'Received'  : Received,
        "Moving"  : Sender.objects.filter(user=request.user, status=Moving).count(),
        'sent' : Sender.objects.filter(user=request.user).count()
    })




# sending a shipment form
@login_required(login_url='cargo_login')
def sent_shipment(request):
    submitted = False
    if request.method == 'POST':
        form = SenderForm(request.POST)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect('sent_shipment?submitted=True')           
           
    else:
        form = SenderForm()
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request, 'cargo/shipment_sending.html',{
        'form'  : SenderForm(),
        "submitted" : submitted 
                 } )
    
 
 
 
    
submitted2 = False
# sending a shipment form
@login_required(login_url='cargo_login')
def receiver_form(request):
    submitted2 = False
    if request.method == 'POST':
        form = ReceiverForm(request.POST)
        name = request.POST['name']
        country = request.POST['country']
        receiver_email = request.POST['email']
        city = request.POST['city']
        length_cm =  int(request.POST['length']) # in centimeters
        width_cm = int(request.POST['width'])  # in centimeters
        height_cm = int(request.POST['height'])  # in centimeters
        actual_weight = int(request.POST['weight'])  # in pounds
        dimensional_factor_cm = 5000  # specific to the carrier, varies by region
        rate_per_unit_weight = 10.0  # in dollars per pound
        destination_based_shipping_cost = 50.99  # Example additional cost based on the destination

        
        
        
        
        
        if form.is_valid():
            
            form = form.save(commit=False)
            
            # Calculate dimensional weight
            dimensional_weight = calculate_dimensional_weight(length_cm, width_cm, height_cm, dimensional_factor_cm)

            # Calculate base shipping cost
            base_shipping_cost = calculate_base_shipping_cost(actual_weight, dimensional_weight, rate_per_unit_weight)

            # Calculate total shipping cost
            total_shipping_cost = calculate_total_shipping_cost(base_shipping_cost, destination_based_shipping_cost)
            
                        
            
            # send mail
               
            # Load the email template
            email_template = get_template('cargo/blank.html')

            # Render the template with context
            email_content = email_template.render({'recipient_name': name, 'Country': country, 'City': city, 'dimensional_weight': dimensional_weight,
                                                   "base_shipping_cost": base_shipping_cost, "total_shipping_cost": total_shipping_cost })

            # Create an EmailMultiAlternatives object
            email = EmailMultiAlternatives(
                subject='Delivery Request From CRR',
                body=email_content,
                from_email= settings.EMAIL_HOST_USER,
                to=[receiver_email, 'info@cargorouterunner.site']
            )

            # Attach HTML content to the email
            email.attach_alternative(email_content, "text/html")

            # Send the email
            email.send()
        
            
            
            form.user = request.user
            form.save()
            return HttpResponseRedirect('receiver_form?submitted2=True2')           
           
    else:
        form = ReceiverForm()
        if 'submitted2' in request.GET:
            submitted2 = True
    

    return render(request, 'cargo/shipment_sending.html',{
        'form'  : ReceiverForm(),
        "submitted2" : submitted2
                 } )






# Track a shipment

def tracking_shipment(request):
    
    sendings  = Sender.objects.all()
    Received ="Received"
    return render(request, 'cargo/shipment_tracking.html',{
        "sendings" : sendings ,
        'Received'  : Received
    })



# Recieveing a shipment
def receiving_shipment(request):
    return render(request, 'cargo/shipment_receiving.html')




@login_required(login_url='cargo_login')
def shipment_table(request):
    sending = Sender.objects.all()
    receiving = Reciever.objects.all()
    return render(request, 'cargo/tables.html',{
        "sendings": sending,
        "receivings" : receiving 
    })
  
  
  

# Search form 
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        custom_id = request.POST['custom_id']
        if form.is_valid():            
            
            return redirect('search_info', custom_id=custom_id)
    else:
        form = SearchForm()
    return render(request, 'faster/index.html', {'form': form}) 

  
  
    
def search_info(request, custom_id):
    instance = get_object_or_404(Reciever, custom_id=custom_id)
    return render(request, 'cargo/tracker.html', {'instance': instance}) 



