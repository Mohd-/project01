from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client, Customer

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    phone_no = forms.CharField(max_length=20, help_text='please enter your phone number.')
    type = forms.ChoiceField(choices=[('client', 'Client'), ('customer', 'Customer')])
    if type == 'client' or 'Client':
        tier = forms.ChoiceField(choices=[('1','1'),('2','2'),('3','3')])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'type','tier')
