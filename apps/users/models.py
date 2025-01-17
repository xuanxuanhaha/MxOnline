from django.db import models

# 继承这个类
from django.contrib.auth.models import AbstractUser

from datetime import datetime
# Create your models here.


GENDER_CHOICES=(
    ("male", "男"),
    ("female", "女")
)


# 这个model是希望被其他model继承的。
class BaseModel(models.Model):
    # now不要加括号，原因在于不希望时间是创建Course类的时候，而是希望在实例化的时候才记录当时的时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    # 不希望这个BaseModel生成表
    class Meta:
        abstract = True


# 定义自己的user
class UserProfile(AbstractUser):
    # 昵称可以为空
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 手机字段不可以为空，并且需要唯一
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    # Y:年， m:月
    image = models.ImageField(upload_to="head_image/%Y/%m", default="default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    #当得到用户profile时候，字符串在描述什么，会怎么print对象呢
    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username