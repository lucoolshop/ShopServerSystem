import os

from django.shortcuts import render
import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from common import md5_
from adminapp.models import SysUser, SysRole

from Shopms import settings
# Create your views here.
from msgapp.models import Message, Feedback
from productapp.models import Category, Products, Source
from userapp.models import User


def login(request):
        # 分两种用户，一个是会员，一个管理员（系统）
        print('--->', request.method)
        if request.method == 'POST':
            print(request.POST)

            error = None

            username = request.POST['username'].strip()
            password = request.POST['password'].strip()
            remeber = request.POST.get('remeber', '')  # checkbox

            password_ = md5_.hash_encode(password)  # 转成md5后的密文

            # 验证用户名和口令是否为空
            if not all((username, password)):
                error = f'用户名或口令不能为空！'

            login_user = SysUser.objects.filter(username=username, auth_string=password_).first()
            if login_user:
                # 系统管理员
                role_ = login_user.role
                login_info = {
                    '_id': login_user.id,
                    'name': role_.name,
                    'code': role_.code
                }

            else:
                login_user = User.objects.filter(
                    (Q(user_name=username) or Q(user_phone=username)) and Q(auth_string=password)).first()
                if login_user:
                    login_info = {
                        'user_id': login_user.user_id,
                        'user_img': login_user.user_img,
                        'user_name':login_user.user_name,
                        'user_phone': login_user.user_phone,
                    }
                else:
                    error = f'{username} 用户名或口令错误！'

            if not error:
                request.session['login_user'] = login_info
                return redirect('/')

        return render(request, 'login.html', locals())

def index(request):
    return render(request,'dashboard.html')

def role(request):
    action = request.GET.get('action', '')
    if action == 'del':
        SysRole.objects.get(pk=request.GET.get('role_id')).delete()

    roles = SysRole.objects.all()
    return render(request, 'role/list.html', locals())



def logout(request):
    del request.session['login_user']
    return redirect('/login/')

def list_sys_user(request):
    action = request.GET.get('action', '')
    if action == 'del':
        SysUser.objects.get(pk=request.GET.get('id_')).delete()
    users = SysUser.objects.filter(~Q(pk=request.session['login_user']['_id'])).all()
    return render(request, 'sys_user/list.html', locals())

class EditRoleView(View):
    def get(self, request):
        role_id = request.GET.get('role_id', '')
        if role_id:
            role = SysRole.objects.get(pk=role_id)
        return render(request, 'role/edit.html', locals())

    def post(self, request):
        from .forms import RoleForm
        role_id = request.POST.get('id', '')
        if role_id:
            form = RoleForm(request.POST, instance=SysRole.objects.get(pk=role_id))
        else:
            form = RoleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/role/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'role/edit.html', locals())

class EditSysUserView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = SysUser.objects.get(pk=id_)

        roles = SysRole.objects.filter(~Q(code='admin'))
        return render(request, 'sys_user/edit.html', locals())

    def post(self, request):
        from .forms import SysUserForm
        sys_id = request.POST.get('id', '')
        if sys_id:
            form = SysUserForm(request.POST, instance=SysUser.objects.get(pk=sys_id))
        else:
            form = SysUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/list_sysuser/')

        errors = json.loads(form.errors.as_json())

        roles = SysRole.objects.filter(~Q(code='admin'))

        return render(request, 'sys_user/edit.html', locals())
def message(request):
    objs = Message.objects.all()
    action = request.GET.get('action', '')
    if action == 'del':
        Message.objects.get(pk=request.GET.get('id_')).delete()
    return render(request, 'message/list.html', locals())

class EditMessageView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = Message.objects.get(pk=id_)

        return render(request, 'message/edit.html', locals())

    def post(self, request):
        from .forms import MessageForm
        id_ = request.POST.get('id_', '')
        if id_:
            form = MessageForm(request.POST, instance= Message.objects.get(pk=id_))
        else:
            form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/message/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'message/edit.html', locals())


class AuditMessage(View):
    def get(self, request):
        action = request.GET.get('action', '')
        if action:
            obj = Message.objects.get(pk=request.GET.get('id_'))
            if action == 'yes':
                obj.state = 1
            elif action == 'no':
                obj.state = 2
                obj.note=request.GET.get('note', '')
            obj.save()
            obj.full_clean()
        objs = Message.objects.filter(state=0).all()
        return render(request, 'message/list_audit.html', locals())

def check_category(request):
    action = request.GET.get('action', '')
    if action == 'del':
        Category.objects.get(pk=request.GET.get('category_id')).delete()

    categories = Category.objects.all()
    return render(request, 'product/category_list.html', locals())


class EditcategoryView(View):
    def get(self, request):
        category_id = request.GET.get('category_id', '')
        if category_id:
            category = Category.objects.get(pk=category_id)
        return render(request, 'product/category_edit.html', locals())

    def post(self, request):
        from .forms import CateGory
        category_id = request.POST.get('category_id', '')
        if category_id:
            form = CateGory(request.POST, instance=Category.objects.get(pk=category_id))
        else:
            form = CateGory(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/category/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'product/category_edit.html', locals())

def list_source(request):
        action = request.GET.get('action', '')
        if action == 'del':
            Source.objects.get(pk=request.GET.get('source_id')).delete()

        sources = Source.objects.all()
        return render(request,'product/source_list.html', locals())


class EditsourceView(View):
    def get(self, request):
        source_id = request.GET.get('source_id', '')
        if source_id:
            source = Source.objects.get(pk=source_id)
        return render(request, 'product/source_edit.html', locals())

    def post(self, request):
        from .forms import SouRce
        source_id = request.POST.get('id', '')
        if source_id:
            form = SouRce(request.POST, instance= Source.objects.get(pk=source_id))
        else:
            form = SouRce(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/list_source/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'product/source_edit.html', locals())




def list_user(request):
    action = request.GET.get('action', '')
    if action == 'del':
        User.objects.get(pk=request.GET.get('user_id')).delete()

    users = User.objects.all()
    return render(request, 'users/list.html', locals())


class EdituserView(View):
    def get(self, request):
        user_id = request.GET.get('user_id', '')
        if user_id:
            user = User.objects.get(pk=user_id)
        return render(request, 'users/list.html', locals())

    def post(self, request):
        from .forms import USer
        user_id = request.POST.get('id', '')
        if user_id:
            form = USer(request.POST, instance= User.objects.get(pk=user_id))
        else:
            form = USer(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/list_user/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'users/edit.html', locals())


def feedback(request):
    action = request.GET.get('action', '')
    if action == 'del':
        Feedback.objects.get(pk=request.GET.get('feedback_id')).delete()
    feedbacks = Feedback.objects.all()
    return render(request, 'message/feedback.html', locals())


def list_product(request):
    action = request.GET.get('action', '')
    if action == 'del':
        Products.objects.get(pk=request.GET.get('id_')).delete()

    products = Products.objects.all()
    return render(request, 'product/product_list.html', locals())


class EditproductView(View):
    def get(self, request):
        source_id = request.GET.get('id_', '')
        if source_id:
            product = Products.objects.get(pk=source_id)
        sources = Source.objects.all()
        categorys = Category.objects.all()
        return render(request, 'product/product_edit.html', locals())


    def post(self, request):
        from .forms import ProductsForm
        product_id = request.POST.get('product_id', '')
        is_update = request.POST.get('is_update', '')
        if is_update:
            if product_id:
                try:
                    old_source = Products.objects.filter(pk=product_id)
                    if not request.FILES.get('product_img'):
                        request.FILES['product_img'] = old_source.first().product_img
                    else:
                        path = "/s/shops_img/" + str(product_id)
                        with open(os.path.join("static/shops_img",str(product_id)),"wb") as f:
                            f.write(request.FILES.get('product_img').read())
                            request.FILES['product_img'] = path
                    if old_source:
                        old_source.update(product_id=request.POST.get('product_id', ''),
                                          source_id=request.POST.get('source_id', ''),
                                          product_img=request.FILES.get('product_img'),
                                          category_name=request.POST.get('category_name', ''),
                                          product_name=request.POST.get('product_name', ''),
                                          product_priceout=request.POST.get('product_priceout', ''),
                                          product_longname=request.POST.get('product_longname', ''),
                                          product_storenum=int(request.POST.get('product_storenum', '')),
                                          product_numout=int(request.POST.get('product_numout', '')),
                                          product_time=int(request.POST.get('product_time', '')),
                                          product_expiretime=int(request.POST.get('product_expiretime', '')),
                        )
                        return redirect('/list_product/')
                    else:
                        print('id不存在')
                        return render(request, 'product/product_edit.html')
                except Exception as e:
                    print(e)
        if product_id:
            if Products.objects.filter(pk=product_id):
                return render(request, 'product/product_edit.html', locals())
            else:
                path = "/s/shops_img/" + str(product_id)
            if request.FILES.get('product_img'):
                with open(os.path.join("static/shops_img", str(product_id)), "wb") as f:
                    f.write(request.FILES.get('product_img').read())
                    request.FILES['product_img'] = path
            Products.objects.create(product_id=request.POST.get('product_id', ''),
                                    source_id=request.POST.get('source_id', ''),
                                    product_img=request.FILES.get('product_img','/s/images/thumbs/avatarbig.png'),
                                    category_name=request.POST.get('category_name', ''),
                                    product_name=request.POST.get('product_name', ''),
                                    product_priceout=request.POST.get('product_priceout', ''),
                                    product_longname=request.POST.get('product_longname', ''),
                                    product_storenum=int(request.POST.get('product_storenum', '')),
                                    product_numout=int(request.POST.get('product_numout', '')),
                                    product_time=int(request.POST.get('product_time', '')),
                                    product_expiretime=int(request.POST.get('product_expiretime', '')),)
            return redirect('/list_product/')
        else:
            form = ProductsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
            return redirect('/list_product/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'product/product_edit.html', locals())


def list_indent(request):
    return None