from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=30,verbose_name='课程名称')
    info=models.CharField(max_length=300,verbose_name='课程描述')
    detail=models.TextField(verbose_name='课程详情')
    difficulty=models.CharField(max_length=20,choices=(('gj','高级'),('zj','中级'),('cj','初级')))
    learning_times=models.FloatField(default=0,verbose_name='学习时长（分钟）')
    students=models.IntegerField(verbose_name='学生人数',default=0)
    collect_nums=models.IntegerField(verbose_name='收藏人数',default=0)
    cover=models.ImageField(verbose_name='课程封面',upload_to='cover/',null=True)
    click_num=models.IntegerField(verbose_name='点击数',default=0)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

    class Meta:
        verbose_name='课程'
        db_table='course'

    def __unicode__(self):
        #章节的外键是课程，重载其方法
        return self.name


class Lesson(models.Model):
    course=models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    #与课程一对多关系，通过外键进行映射
    name=models.CharField(verbose_name='章节',max_length=200)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

    class Meta:
        verbose_name='章节'
        db_table='lesson'

class Video(models.Model):
    lesson=models.ForeignKey(Lesson,verbose_name='章节',on_delete=models.CASCADE)
    name=models.CharField(verbose_name='视频',max_length=300)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

    class Meta:
        verbose_name='视频'
        db_table='video'

class CourseResource(models.Model):
    course=models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name=models.CharField(max_length=300,verbose_name='名称')
    download=models.FileField(verbose_name='下载地址',upload_to='course_resource/',null=True)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

    class Meta:
        verbose_name='下载地址'
        db_table='course_resource'

