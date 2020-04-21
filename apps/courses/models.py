from django.db import models

# import 自己定义的Model，是在users里面，因为users在最底层
from apps.users.models import BaseModel
from apps.organizations.models import Teacher

# Create your models here.
# 实体1 - 关系 - 实体2
# 课程 章节 视频 课程资源

# 找到课程实体的具体字段
# 每一个字段的类型，是否必填

class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="讲师")
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")
    degree = models.CharField(verbose_name="难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name="课程类别")
    tag = models.CharField(default="", verbose_name="课程标签", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name="课程须知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="老师告诉你")

    detail = models.TextField(verbose_name="课程详情")
    image = models.ImageField(upload_to="courses/%Y/%m", default="封面图", max_length=100)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name


# 章节信息
class Lesson(BaseModel):
    # 外键, on_delete表示对应的外键数据被删除后，当前的数据应该怎么办，CASCADE是也删除的意思，不要括号
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u"章节名", max_length=100)
    learn_times = models.IntegerField(verbose_name=u"学习时长（分钟数）", default=0)

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name


# 视频信息
class Video(BaseModel):
    # 外键, on_delete表示对应的外键数据被删除后，当前的数据应该怎么办，CASCADE是也删除的意思，不要括号
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="章节")
    name = models.CharField(verbose_name=u"视频名", max_length=100)
    learn_times = models.IntegerField(verbose_name=u"学习时长（分钟数）", default=0)
    url = models.CharField(verbose_name=u"访问地址", max_length=200)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


# 课程资源
class CourseResource(BaseModel):
    # 外键, on_delete表示对应的外键数据被删除后，当前的数据应该怎么办，CASCADE是也删除的意思，不要括号
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(verbose_name=u"名称", max_length=100)
    file = models.FileField(verbose_name="下载地址", upload_to="course/resourse/%Y/%m", max_length=200)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name