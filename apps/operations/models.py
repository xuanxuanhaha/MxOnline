from django.db import models

from apps.users.models import BaseModel
from apps.courses.models import Course

# 之前在settings里面配置过，这个get_user_model就是userprofile表
from django.contrib.auth import get_user_model

UserProfile = get_user_model()

# 用户咨询框框输入的信息
class UserAsk(BaseModel):
    # 用户可以不登陆就填写信息，所以不需要外键
    name = models.CharField(verbose_name=u"姓名", max_length=20)
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

class CourseComment(BaseModel):
    # 用户必须评论才可以填写
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    course = models.ForeignKey(Course, verbose_name="课程")
    comments = models.CharField(max_length=200, verbose_name="评论内容")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

# 用户收藏：favorite
class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    fav_id = models.IntegerField(verbose_name="数据ID")
    fav_type = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师 ")), default=1, verbose_name=u"收藏类型")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


# 用户收藏：favorite
class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    message = models.CharField(verbose_name="消息内容", max_length=200)
    has_read = models.BooleanField(default=False, verbose_name="是否已读")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

# 我的课程
class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    course = models.ForeignKey(Course, verbose_name="课程")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name