from django.db import models


# Create your models here.
from productapp.models import Products
from userapp.models import UserAddress


class Indent(models.Model):
    indent_id = models.IntegerField(primary_key=True)
    address = models.ForeignKey(UserAddress, models.DO_NOTHING)
    indent_time = models.DateField()
    indent_price = models.FloatField()
    indent_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indent'

class IdentMsg(models.Model):
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    indent = models.ForeignKey(Indent, models.DO_NOTHING, blank=True, null=True)
    ident_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ident_msg'
