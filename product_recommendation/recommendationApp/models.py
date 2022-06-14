# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

class Product(models.Model):
	name=models.CharField(max_length=50)
	product_description=models.CharField(max_length=200)
	price=models.IntegerField()
	product_type=models.CharField(max_length=50)
	seasonal=models.CharField(max_length=50)
	brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name = 'brand_name')


class Order(models.Model):
	quantity=models.IntegerField()
	product_id=models.ForeignKey(Product, on_delete=models.CASCADE,related_name = 'product_detail')
	name=models.CharField(max_length=50)
	phone=models.IntegerField()
	address=models.CharField(max_length=200)
	pinCode=models.IntegerField()
