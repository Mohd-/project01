from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from django.http import HttpResponse
from django.template import loader
from .models import Client, Customer

def index(request):
    return HttpResponse("This is the main page")



def register(request): #should be signup
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data['type'] == 'client':
                Client.objects.create(user=user)
            else:
                Customer.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'tickets/register.html', {'form': form})
