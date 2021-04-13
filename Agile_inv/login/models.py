from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length = 60)
    lastName = models.CharField(max_length=60)
    userName= models.CharField(max_length = 60)
    password= models.CharField(max_length = 60)
    role=models.CharField(max_length = 60)
    def __str__(self):
        return f'User name:{self.firstName} Role: {self.role}'

# Create your models here.
