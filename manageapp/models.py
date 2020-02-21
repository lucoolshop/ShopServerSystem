from django.db import models

class Managers(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=10)
    password = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'managers'

