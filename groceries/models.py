from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    api_url = models.URLField()
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_date = models.DateField()
    location = models.CharField(max_length=100)

class UserPreference(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    preferred_location = models.CharField(max_length=100)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.TextField()