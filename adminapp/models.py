from django.db import models

from common import md5_


class SysRole(models.Model):
    name = models.CharField(unique=True, max_length=20)
    code = models.CharField(unique=True, max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role'

class SysUser(models.Model):
    username = models.CharField(unique=True, max_length=20)
    auth_string = models.CharField(max_length=32)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    @property
    def role(self):
        return SysRole.objects.get(pk=self.role_id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.auth_string) != 32:
            self.auth_string = md5_.hash_encode(self.auth_string)

    class Meta:
        managed = False
        db_table = 'sys_user'



class SysMenu(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    ord = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_menu'

class SysRoleMenus(models.Model):
    role_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role_menus'
