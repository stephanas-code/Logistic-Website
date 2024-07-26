from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *




class SenderForm(forms.ModelForm):
    class Meta:
        model = Sender
        fields = ['name', 'country','city','email' ,'phone']
        
class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Reciever
        fields = ['name', 'country','city','email' ,'phone','message','weight','length','width','height']



class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', "email", 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class SearchForm(forms.Form):
    class Meta:
        model = Reciever
        fields = ['custom_id',]