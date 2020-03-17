from datetime import datetime

from django.db import models

class Source(models.Model):
    id = models.IntegerField(primary_key=True)
    source_address = models.CharField(max_length=100)
    source_product_name = models.CharField(max_length=50)
    unit_price = models.FloatField()
    total_price = models.FloatField()
    source_telephone = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    source_number = models.IntegerField()
    create_time = models.DateTimeField()

    @property

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.create_time is None:
            self.create_time = datetime.now()
        super(Source, self).save()

    class Meta:
        managed = False
        db_table = 'source'
        ordering = ['-create_time']
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    source = models.ForeignKey(Source, models.DO_NOTHING)
    category_name = models.CharField(max_length=20)
    product_img = models.CharField(max_length=256, blank=True)
    product_name = models.CharField(max_length=20)
    product_priceout = models.FloatField()
    product_longname = models.CharField(max_length=20, blank=True, null=True)
    product_storenum = models.IntegerField()
    product_numout = models.IntegerField()
    product_time = models.CharField(max_length=50, blank=True, null=True)
    product_expiretime = models.IntegerField(16)


    class Meta:
        managed = False
        db_table = 'products'







class Discount(models.Model):
    discount_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    discount_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount'
