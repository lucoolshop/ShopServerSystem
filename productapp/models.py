from django.db import models

class Source(models.Model):
    source_id = models.IntegerField(primary_key=True)
    source_factory = models.CharField(max_length=20)
    source_total = models.IntegerField()
    source_price = models.FloatField()
    source_all_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'source'

class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    source = models.ForeignKey(Source, models.DO_NOTHING)
    product_img = models.CharField(max_length=256, blank=True, null=True)
    product_name = models.CharField(max_length=20)
    product_priceout = models.FloatField()
    product_longname = models.CharField(max_length=20, blank=True, null=True)
    product_makeprice = models.FloatField()
    product_storenum = models.IntegerField()
    product_numout = models.IntegerField()
    product_time = models.DateField()
    product_expiretime = models.DateField()

    class Meta:
        managed = False
        db_table = 'products'

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    category_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'





class Discount(models.Model):
    discount_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    discount_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount'
