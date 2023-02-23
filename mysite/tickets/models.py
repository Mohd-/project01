from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Client(User):
    tier = 'inactive'
    def __str__(self):
        return self.name
