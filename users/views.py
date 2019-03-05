from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单    
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
			# 检查账号密码是否通过身份验证
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])  #密码被输入两次，但1，2都一样
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    # 将给定的模板与给定的上下文字典组合在一起，并以渲染的文本返回一个 HttpResponse 对象。
    return render(request, 'users/register.html', context)