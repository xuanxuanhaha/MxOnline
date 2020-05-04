from django.shortcuts import render

from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.users.forms import Loginform

# 处理get请求，重载get方法
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        # 重定向到首页
        return HttpResponseRedirect(reverse("index"))


# 同时处理get和post请求
class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # 重定向到首页
            return HttpResponseRedirect(reverse("index"))
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        login_form = Loginform(request.POST)

        if login_form.is_valid():

            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]

            # 表单验证

            # 用于通过用户和密码查询用户是否存在
            user = authenticate(username=user_name, password=password)
            if user is not None:
                # 查询到用户
                login(request, user)
                # 登陆成功之后应该怎么返回页面
                return HttpResponseRedirect(reverse("index"))
            else:
                # 未查询到用户
                return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})
        else:
            return render(request, "login.html", {"login_form": login_form})