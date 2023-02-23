from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Customer(User):
    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    title = models.CharField(max_length=450)
    date_time = models.DateTimeField('date and time of the event')
    capacity = models.IntegerField(default=0)

class Client(User):
    tier = 'inactive'
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    def create_reservation(title, date_time, capacity):
        return Reservation(title, date_time, capacity)
    def __str__(self):
        return self.name