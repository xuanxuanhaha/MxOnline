from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile

# 对这个表创建管理器
class UserProfileAdmin(admin.ModelAdmin):
    pass

# 表的class，管理器的class
# admin.site.register(UserProfile, UserAdmin)