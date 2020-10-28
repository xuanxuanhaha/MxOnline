"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin

from apps.users.views import LoginView
from apps.users.views import LogoutView
from apps.organizations.views import OrgView
from MxOnline.settings import MEDIA_ROOT

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    # 机构相关页面
    url(r'^org_list/', OrgView.as_view(), name="org_list"),

    # 配置上传文件的访问url
    # 后边取出的所有字符串， 放到变量中，并传到后面path的变量名称中。
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
]

