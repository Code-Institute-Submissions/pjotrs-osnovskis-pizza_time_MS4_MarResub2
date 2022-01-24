from sre_parse import CATEGORIES
from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    full_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.full_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    ingredients = models.TextField()
    price_s = models.DecimalField(max_digits=4, decimal_places=2)
    price_m = models.DecimalField(max_digits=4, decimal_places=2)
    price_l = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name