from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Client, Customer

def index(request):
    return HttpResponse("This is the main page")

def register(request):
    #template = loader.get_template('tickets/register.html')
    context = {
        Client : 'client',
        Customer : 'customer',
    }
    return render(request,'tickets/register.html', context)
