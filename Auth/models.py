from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    cin     = models.CharField(max_length=30)
    username= models.CharField(max_length=30,primary_key=True)   
    password= models.CharField(max_length=255)
    poste   = models.CharField(max_length=30,default="technicien")
    email   = models.EmailField()
    telephone= models.CharField(max_length=30)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','password','poste']