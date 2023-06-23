from django.db import models
from django.contrib.auth.models import User

class CakeType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Taste(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Filling(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    cake_types = models.ManyToManyField(CakeType, blank=True)
    tastes = models.ManyToManyField(Taste, blank=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    cake_types = models.ManyToManyField(CakeType, blank=True)
    tastes = models.ManyToManyField(Taste, blank=True)

    def __str__(self):
        return self.name


class Cake(models.Model):
    image = models.ImageField(upload_to='cakes/', blank=True, null=True)
    cake_type = models.ForeignKey(CakeType, on_delete=models.SET_NULL, null=True, blank=True)
    taste = models.ForeignKey(Taste, on_delete=models.SET_NULL, null=True, blank=True)
    fillings = models.ManyToManyField(Filling, blank=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(default=True)
    add_info = models.TextField(blank=True, null=True)  # новое поле

    def __str__(self):
        return self.cake_type.name + ' ' + self.taste.name + ' ' + str(self.weight) + ' кг'


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cakes = models.ManyToManyField(Cake)