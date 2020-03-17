
from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=256, blank=True, null=True)
    user_name = models.CharField(max_length=20)
    auth_string = models.CharField(max_length=20)
    phone = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'

class UserAddress(models.Model):
    address_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    address = models.CharField(max_length=256)
    telephone = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_address'

class Grade(models.Model):
    grade_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    grade = models.CharField(max_length=10)
    intergration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grade'
