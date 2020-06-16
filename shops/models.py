from django.db import models
from users.models import User


class Shop(models.Model):
    title = models.CharField(max_length=512, unique=True)
    description = models.TextField()
    founder = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='static/shop_image/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        indexes = [
            models.Index(fields=['title', 'description'])
        ]

    @property
    def test_shop(self):
        return self.title, self.description, self.founder, self.thumbnail


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    @property
    def test_category(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True, default=None)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', related_name='Item')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    @property
    def test_item(self):
        return self.title, self.description, self.shop, self.category, self.price, self.quantity


class ItemImage(models.Model):
    item = models.ForeignKey(Item, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')
    is_active = models.BooleanField(default=True)

# Create your models here.
