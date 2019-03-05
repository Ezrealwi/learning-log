"""为应用程序users定义URL模式"""

from django.urls import path,re_path
from django.contrib.auth.views import LoginView #导入类

from . import views

# LoginView.template_name = 'users/login.html'
urlpatterns = [
    # 登陆界面
    # path('login/',LoginView.as_view(),name='login'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('register/', views.register,name='register'),
]
app_name = 'users'