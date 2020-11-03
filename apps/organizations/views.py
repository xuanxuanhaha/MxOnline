from django.shortcuts import render
from django.views.generic.base import View

from apps.organizations.models import CourseOrg
from apps.organizations.models import City
from MxOnline.settings import MEDIA_URL
# Create your views here.
class OrgView(View):
    # Get方法
    def get(self, request, *args, **kwargs):
        # 从数据库中获取数据
        all_orgs = CourseOrg.objects.all()
        org_nums = CourseOrg.objects.count()
        all_citys = City.objects.all()

        # 展示数据
        return render(request, "org-list.html", {
            "all_orgs": all_orgs,
            "org_nums": org_nums,
            "all_citys": all_citys
        })
