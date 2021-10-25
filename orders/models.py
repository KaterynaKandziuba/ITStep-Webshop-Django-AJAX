from django.db import models
from goods.models import Product
from django.contrib.auth.models import User
from django.utils import timezone

class Order(models.Model):
    
    customer = models.TextField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.FloatField()
    delivery = models.TextField(max_length=500)
    details = models.TextField(max_length=500)


    def __str__(self) -> str:
        return str(self.product) + ': ' + str(self.amount)

class Order_C(models.Model):
    
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    amount = models.IntegerField()
    status = models.CharField(max_length=100)


    def __str__(self) -> str:
        return str(self.title)