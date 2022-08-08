from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField('название', max_length=255)
    image = models.ImageField(blank = True, null = True)

    def get_link(self):
        return reverse ('category_detail_url',kwargs = {'id':self})
    
    class Meta:
        verbose_name ='категория'
        verbose_name_plural ='категории'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField('название', max_length=255)
    price = models.IntegerField('цена', default="0")
    image = models.ImageField(blank = True, null = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='favourite_product')
    text = models.TextField('описание', default="text")
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def get_link(self):
        return reverse ('product_detail_url',kwargs = {'id':self})

    class Meta:
        verbose_name ='продукт'
        verbose_name_plural ='продукты'

    def __str__(self):
        return self.title

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
