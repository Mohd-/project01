from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #name = models.CharField(max_length=200)
    #email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #name = models.CharField(max_length=200)
    #email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    tier = models.CharField(max_length=200)
    def __str__(self):
        return self.user.username
    
class Reservation(models.Model):
    title = models.CharField(max_length=450)
    date_time = models.DateTimeField('date and time of the event')
    capacity = models.IntegerField(default=0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    def __str__(self):
        return self.reservation.title