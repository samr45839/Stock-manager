from django.utils import timezone
from django.db import models


# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=64)
    mail = models.EmailField(null=True)
    contact = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name


class Client_Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Product(models.Model):
    matcode = models.DecimalField(max_digits=11, decimal_places=0, null=True, blank='True')
    name = models.CharField(max_length=64)
    model = models.CharField(max_length=64, blank='True')
    description = models.TextField(blank='True')
    serial_number = models.DecimalField(max_digits=11, decimal_places=0, null=True, blank='True')
    waranty = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank='True')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank='True')
    sale_price = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank='True')
    purchase_price = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank='True')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{} rest {}'.format(self.name, self.quantity)


class Client(models.Model):
    name = models.CharField(max_length=64)
    contact = models.CharField(max_length=25, blank=True)
    mail = models.EmailField(blank=True)
    company = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Client_Category, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    product = models.ManyToManyField(Product, through='Order_Client', blank=True)

    def __str__(self):
        return self.name


class Order_Client(models.Model):
    date = models.DateField(default=timezone.now)
    quantity = models.PositiveSmallIntegerField(default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{} by {}'.format(self.date, self.quantity)

    class Meta:
        ordering = ['date']


"""
class Order_Provider(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.price
"""
