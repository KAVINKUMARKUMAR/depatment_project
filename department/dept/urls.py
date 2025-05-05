from django.urls import path
from . import views

urlpatterns = [
    path('dept/register', views.Adddept.as_view(), name = 'adddept'),
    path('dept/edit/<int:pk>', views.Editdept.as_view(), name = 'editdept'),
    path('dept/delete/<int:pk>', views.deldept.as_view(), name = 'deldept'),
    path('dept/del/<int:pk>', views.conf_del, name = 'conf_del'), 
    path('',views.dept_det,name='dept_det')   
]