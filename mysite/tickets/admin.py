from django.contrib import admin
from .models import Client, Customer, Reservation

admin.site.register(Reservation)
admin.site.register(Client)
admin.site.register(Customer)