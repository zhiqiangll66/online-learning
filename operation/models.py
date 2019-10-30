from django.db import models
from users.models import UserProfile
from course.models import Course


# Create your models here.
class UserAsk(models.Model):
    name=models.CharField(verbose_name='姓名',max_length=20)
    mobile=models.CharField(verbose_name='手机',max_length=11)
    course_name=models.CharField(verbose_name='课程名称',max_length=30)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

    class Meta:
        verbose_name='用户咨询'
        db_table='user_ask'


class CourseComment(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course=models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    comments=models.CharField(verbose_name='评论',max_length=300)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

    class Meta:
        verbose_name='课程评论'
        db_table='course_comment'


class UserStore(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    store_id=models.IntegerField(default=0,verbose_name='数据id')
    store_type=models.IntegerField(choices=((1,'课程'),(2,'课程机构'),(3,'教师')),default=1,verbose_name='收藏')
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

    class Meta:
        verbose_name='用户收藏'
        db_table='user_store'


class UserMessg(models.Model):
    user=models.IntegerField(default=0,verbose_name='接收用户')
    messg=models.CharField(verbose_name='消息内容',max_length=300)
    has_read=models.BooleanField(default=False,verbose_name='是否已读')
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now=True)

    class Meta:
        verbose_name='用户消息'
        db_table='user_messg'


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now=True)

    class Meta:
        verbose_name='用户课程'
        db_table='user_course'

