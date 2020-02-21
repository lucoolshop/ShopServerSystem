from django.db import models

from indentapp.models import Indent
from userapp.models import User


class Feedback(models.Model):
    feedback_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    feedback_suggest = models.CharField(max_length=200, blank=True, null=True)
    feedback_content = models.CharField(max_length=200, blank=True, null=True)
    feedback_img = models.CharField(max_length=256, blank=True, null=True)
    feedback_phone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'

class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Indent, models.DO_NOTHING, blank=True, null=True)
    comment_time = models.DateField(blank=True, null=True)
    comment_content = models.CharField(max_length=200, blank=True, null=True)
    satisfaction = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
