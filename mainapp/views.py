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
from msgapp.models import Message


def login(request):
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
            role_ = login_user.role
            login_info = {
                '_id': login_user.id,
                'name':role_.name,
                'code': role_.code
            }
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
        id_ = request.POST.get('id', '')
        if id_:
            form = SysUserForm(request.POST, instance=SysUser.objects.get(pk=id_))
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


