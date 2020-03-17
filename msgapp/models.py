from datetime import datetime

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

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    link_url = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    states = (
        (0, '审核中'),
        (1, '已通过'),
        (2, '未通过')
    )
    state = models.IntegerField(choices=states, default=0)

    @property
    def state_label(self):
        return self.states[self.state][-1]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.create_time is None:
            self.create_time = datetime.now()

        super(Message, self).save()

    class Meta:
        managed = False
        db_table = 'message'
        ordering = ['-create_time']
