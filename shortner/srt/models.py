from django.db import models

# Create your models here.
class Slink(models.Model):
    l_id = models.AutoField(primary_key=True)
    l_name = models.CharField(max_length=500)

class Ulink(models.Model):
    name = models.CharField(max_length=90)
    l_id = models.AutoField(primary_key=True)
    l_name = models.CharField(max_length=500)

class Clink(models.Model):
    name = models.CharField(max_length=90)
    l_url =models.CharField(max_length=6)
    l_name = models.CharField(max_length=500)

class Contact(models.Model):
    mail=models.CharField(max_length=40)
    messege = models.CharField(max_length=1000)

