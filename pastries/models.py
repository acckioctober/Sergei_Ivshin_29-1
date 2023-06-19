from django.db import models


class Taste(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Filling(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Cake(models.Model):
    image = models.ImageField(upload_to='cakes/', blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    taste = models.ForeignKey(Taste, on_delete=models.SET_NULL, null=True, blank=True)
    fillings = models.ManyToManyField(Filling, blank=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name