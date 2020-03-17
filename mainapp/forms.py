from django import forms

from adminapp.models import SysRole, SysUser
from msgapp.models import Message
from productapp.models import Category, Source, Products
from userapp.models import User


class RoleForm(forms.ModelForm):

    class Meta:
        model = SysRole
        fields = ['name', 'code']  # '__all__'
        error_messages = {
            'name': {
                'required': '角色名不能为空'
            },
            'code': {
                'required': '角色代码不能为空'
            }
        }

class SysUserForm(forms.ModelForm):

    class Meta:
        model = SysUser
        fields = ['username', 'auth_string', 'role_id', 'nick_name']  # '__all__'
        error_messages = {
            'username': {
                'required': '账号不能为空'
            },
            'auth_string': {
                'required': '口令不能为空'
            },
            'role_id': {
                'required': '系统用户角色不能为空'
            }
        }

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['title', 'content', 'link_url']  # '__all__'
        error_messages = {
            'title': {
                'required': '标题不能为空'
            },
            'link_url': {
                'required': '外部连接不能为空'
            },
            'content':{
                'required': '内容不能为空'
            }
        }

class CateGory(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['category_name']  # '__all__'
        error_messages = {
            'category_name': {
                'required': '商品类名不能为空'
            }
        }

class SouRce(forms.ModelForm):

    class Meta:
        model = Source
        fields = ['id','source_product_name','source_number','source_address','source_telephone','unit_price','total_price','note']  # '__all__'
        error_messages = {
            'source_address': {
                'required': '货源地址不能为空'
            },
            'source_product_name': {
                'required': '进货产品数量不能为空'
            },
            'unit_price': {
                'required': '商品单价不能为空'
            },
            'total_price': {
                'required': '商品总花费不能为空'
            }
        }

class USer(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name','auth_string']
        error_messages = {
            'user_name': {
                'required': '用户名不能为空'
            },
            'auth_string': {
                'required': '口令不能为空'
            }
        }

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['product_id','category_name',
            'product_img','product_name','product_priceout'
            ,'product_longname', 'product_storenum','product_numout'
            ,'product_time', 'product_expiretime']  # '__all__'
        error_messages = {
            'product_id': {
                'required': '商品ID不能为空'
            },
            'category_name': {
                'required': '商品类名不能为空'
            },
            # 'product_img': {
            #     'required': '商品图片不能为空'
            # },
            'product_name': {
                'required': '商品名不能为空'
            },
            'product_priceout': {
                'required': '商品出售价不能为空'
            },
            'product_longname': {
                'required': '商品详细名称不能为空'
            },
            'product_storenum': {
                'required': '商品存储量不能为空'
            },
            # 'product_numout': {
            #     'required': '商品出售量不能为空'
            # },
            # 'product_time': {
            #     'required': '生产日期不能为空'
            # },
            # 'product_expiretime': {
            #     'required': '保质期不能为空'
            # }
        }
