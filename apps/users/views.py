from django.shortcuts import render

from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

# 同时处理get和post请求
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")
    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # 用于通过用户和密码查询用户是否存在
        user = authenticate(username=user_name, password=password)
        if user is not None:
            # 查询到用户
            login(request, user)
            # 登陆成功之后应该怎么返回页面
            return HttpResponseRedirect(reverse("index"))
        else:
            # 未查询到用户
            return render(request, "login.html", {"msg":"用户名或密码错误"})