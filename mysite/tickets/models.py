from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    tier = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
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