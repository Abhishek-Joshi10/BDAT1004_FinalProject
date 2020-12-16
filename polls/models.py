from django.db import models

# Create your models here.
class Product_Chennai(models.Model):
    temp = models.TextField()
    feels_like = models.TextField()
    temp_min = models.TextField()
    temp_max = models.TextField()

class Product_Delhi(models.Model):
    temp = models.TextField()
    feels_like = models.TextField()
    temp_min = models.TextField()
    temp_max = models.TextField()

class Product_Hyderabad(models.Model):
    temp = models.TextField()
    feels_like = models.TextField()
    temp_min = models.TextField()
    temp_max = models.TextField()

class Product_Bangalore(models.Model):
    temp = models.TextField()
    feels_like = models.TextField()
    temp_min = models.TextField()
    temp_max = models.TextField()

class Country(models.Model):
    index = models.IntegerField()
    city = models.CharField(max_length=100)
    temp = models.TextField()
    feels_like = models.TextField()
    temp_min = models.TextField()
    temp_max = models.TextField()