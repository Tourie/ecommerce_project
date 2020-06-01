from django.db import models
from users.models import User


class Shop(models.Model):
    title = models.CharField(max_length=512, unique=True)
    description = models.TextField()
    founder = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True, default=None)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    #created = models.DateTimeField(auto_now_add=True, auto_now=False)
   # updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')
    #created = models.DateTimeField(auto_now_add=True, auto_now=False)
   # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
# Create your models here.
