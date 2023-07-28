from django.db import models

class Staff(models.Model):
    firstname = models.CharField(max_length=50)    
    lastname = models.CharField(max_length=50) 
    address = models.CharField(max_length=50)
    dob = models.DateField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
  
    
   