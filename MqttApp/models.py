
from django.db import models

class presion(models.Model):
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)

class msg(models.Model):
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)

class action(models.Model):
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)

class temp(models.Model):
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)

class motor(models.Model):
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)
