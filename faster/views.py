from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from cargo.forms import SearchForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        custom_id = request.POST['custom_id']
        if form.is_valid():            
            
            return redirect('search_info', custom_id=custom_id)
    else:
        form = SearchForm() 
    
    return render(request, "faster/index.html",{
    })
    
def about(request):
    return render(request, 'faster/about.html')

def services(request):
    return render(request, 'faster/services.html')

def contact(request):
    submitted = False
    if request.POST:
        form = ContactForm(request.POST)
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']

        if form.is_valid(): 
            form = form.save(commit=False)
                    
            send_mail(
                f'Sub: {subject}' , #title
               f'Dear {name}, if you are receiving this mail, you have successfully received your submission. We are glad that you have decide to use our services. A member of the support team will reply your and help solve the issue(s). Responses takes 4 to 8 hours.\
               \
                 Thank you.', # message
                settings.EMAIL_HOST_USER ,   # Your email address
                [ email, 'info@cargorouterunner.site'],#receivers email
                fail_silently=False
                

            )
            
            form.save()

            return HttpResponseRedirect("/contact?submitted=True")
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    
    

    return render(request, 'faster/contact.html',{
         "form" : ContactForm(),
        "submitted" : submitted
    })
    
    

def blog(request):
    return render(request, 'faster/blog.html')

def privacy(request):
    submitted = False
    if request.POST:
        form = ContactForm(request.POST)
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']

        if form.is_valid():
            """
            send_mail(
                f'Sub: {subject}' , #title
               f'Dear {name}, if you are receiving this mail, you have successfully received your submission. We are glad that you have decide to use our services. A member of the support team will reply your and help solve the issue(s). Responses takes 4 to 8 hours.\
               \
                 Thank you.\
                 \
                 Stephanas Odogu.\
                 \
                 Chief Executive Officer , ', # message
                settings.EMAIL_HOST_USER,
                [ email, 'stephanas.odogu@cybria.tech'],#receivers email
                fail_silently=False
                

            )
            """
            form.save()

            return HttpResponseRedirect("/privacy?submitted=True")
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'faster/privacy.html', {
        "form" : ContactForm(),
        "submitted" : submitted
    })