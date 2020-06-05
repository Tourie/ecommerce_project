from django.db import models
from users.models import User


class Shop(models.Model):
    title = models.CharField(max_length=512, unique=True)
    description = models.TextField()
    founder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ShopImage(models.Model):
    image = models.ImageField(upload_to='static/shop_image/')


class Item(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True, default=None)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class ItemImage(models.Model):
    item = models.ForeignKey(Item, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')
    is_active = models.BooleanField(default=True)

# Create your models here.
