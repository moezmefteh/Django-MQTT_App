from django.db import models

class presion(models.Model):
    id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)
    def __str__(self):
        return ('presion ' + str(self.id))

class msg(models.Model):
    id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)
    def __str__(self):
        return ('msg ' + str(self.id))

class temp(models.Model):
    id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)
    def __str__(self):
        return ('temp ' + str(self.id))

class action(models.Model):
    id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)
    cmdfromapp =models.CharField(max_length=2)
    def __str__(self):
        return ('action ' + str(self.id))


class motor(models.Model):
    id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)
    cmdfromapp =models.CharField(max_length=2)
    def __str__(self):
        return ('motor ' + str(self.id))

class vanne(models.Model):
    id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField()
    value = models.CharField(max_length=200)
    cmdfromapp =models.CharField(max_length=2)
    def __str__(self):
        return ('vanne ' + str(self.id))