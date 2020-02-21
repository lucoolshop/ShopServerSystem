from django.db import models

# Create your models here.
from productapp.models import Products
from userapp.models import User


class Carts(models.Model):
    carts_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    shopnumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carts'
