from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login),
    path('logout/', views.logout),
    path('message/', views.message),
    path('edit_message/', views.EditMessageView.as_view()),
    path('message_audit/', views.AuditMessage.as_view()),
    path('role/',views.role),
    path('edit_role/', views.EditRoleView.as_view()),
    path('list_sysuser/', views.list_sys_user),
    path('edit_sysuser/', views.EditSysUserView.as_view()),
    path('category/',views.check_category),
    path('edit_category/',views.EditcategoryView.as_view()),
    path('list_source/',views.list_source),
    path('edit_source/',views.EditsourceView.as_view()),
    path('list_user/',views.list_user),
    path('edit_user/',views.EdituserView.as_view()),
    path('feedback/',views.feedback),
    path('list_product/',views.list_product),
    path('edit_product/',views.EditproductView.as_view()),
    path('list_indent/',views.list_indent),
    path('',views.index),
]
