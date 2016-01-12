from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=140)
	slug = models.SlugField(max_length=140, unique=True)
	description = models.TextField()
	is_active = models.BooleanField(default=True)
	meta_keywords = models.CharField("Meta Keywords", max_length=255)
	meta_description = models.CharField("Meta Description", max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Meta:
	db_table = 'categories'
	ordering = ['-created_at']
	verbose_name_plural = 'Categories'
def __unicode__(self):
	return self.name
@models.permalink
def get_absolute_url(self):
	return ('catalog_category',(), { 'category_slug': self.slug })

# UNFINISHED CLASS PRODUCT
class Product(models.Model):
	name = models.CharField(max_length=140)
	slug = models.SlugField()
	description = models.CharField(max_length=500)
	available = models.BooleanField(default=False)
	picture = models.ImageField(upload_to=None, max_length=140)
	sku = models.CharField(max_length=140)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	is_featured =  models.BooleanField(default=False)
	meta_keywords = models.CharField("Meta Keywords", max_length=255)
	meta_description = models.CharField("Meta Description", max_length=255)
	published_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField(Category)
class Meta:
	db_table = 'products'
	ordering = '-published_at'
def __unicode__(self):
	return self.name
@models.permalink
def get_absolute_url(self):
	return ('catalog_product', (), { 'product_slug': self.slug })
