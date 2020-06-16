from django.db import models
from shops.models import *


class Status(models.Model):
    name = models.CharField(max_length=48)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    customer_name = models.CharField(max_length=128)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    comments = models.TextField(blank=True, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)

    def __str__(self):
        return self.status.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        indexes = [
            models.Index(fields=['id'])
        ]


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.title
# Create your models here.
