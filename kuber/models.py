from django.db import models

# Create your models here.
class revs(models.Model):
    name = models.CharField(max_length=30)
    rev = models.TextField()
class reservations(models.Model):
    user = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    date = models.CharField(max_length=11)
    time = models.CharField(max_length=10)
