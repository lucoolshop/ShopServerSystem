from django.db import models


# Create your models here.
from productapp.models import Products
from userapp.models import UserAddress


class Indent(models.Model):
    indent_id = models.IntegerField(primary_key=True)
    address = models.ForeignKey(UserAddress, models.DO_NOTHING)
    product = models.ForeignKey(Products,models.DO_NOTHING)
    indent_time = models.DateField()
    indent_price = models.FloatField()
    indent_state = models.IntegerField()
    pay_state = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'indent'
