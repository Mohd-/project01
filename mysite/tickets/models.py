from django.db import models
from django.contrib.auth.models import User, AbstractUser

#uncomment and use as user model for deployment

#class User(AbstractUser):
#   pass

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=200)

    class Tiers(models.TextChoices):
        frst = '1', 'First'
        scnd = '2', 'Second'
        thrd = '3', 'Third'
    tier = models.CharField(blank=True, choices=Tiers.choices, max_length=200)

    def __str__(self):
        return self.user.username
    
class Reservation(models.Model):
    title = models.CharField(max_length=450)
    date_time = models.DateTimeField('date and time of the event')
    capacity = models.IntegerField(default=0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    cost = models.IntegerField(default=999999)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.reservation.title