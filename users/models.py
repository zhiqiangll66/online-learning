from django.db import models

# Create your models here.
#表名：users_userprofile
#库名：learn
class UserProfile(models.Model):
    nickname=models.CharField(max_length=20,verbose_name='昵称',default='')
    birthday=models.DateField(max_length=30,verbose_name='生日',default='')
    gender=models.CharField(max_length=10,choices=(('male','男'),('female','女')),default='female')
    address=models.CharField(max_length=50,verbose_name='区域',default='')
    phone=models.CharField(max_length=11,verbose_name='手机',null=True,blank=True)
    #null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空，那么在新建一个model对象的时候是不会报错的！！
    #blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
    email=models.EmailField(max_length=30,verbose_name='邮箱')
    name=models.CharField(max_length=20,verbose_name='姓名',default='')
    head_image=models.ImageField(upload_to='head_image/',null=True)
    login_time=models.DateTimeField('登入时间',auto_now=True)

    class Meta:
        db_table = 'users_userprofile'
        verbose_name = '用户信息'


class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=30,verbose_name='邮箱验证码')
    send_type=models.CharField(max_length=20,choices=(('forget','找回密码'),('register','注册')))
    send_time=models.DateTimeField('发送验证时间',auto_now=True)
    email = models.EmailField(max_length=30, verbose_name='邮箱',default='')

    class Meta:
        db_table = 'email_verify_record'
        verbose_name = '邮箱验证'


class Scrollbar(models.Model):
    title=models.CharField(max_length=100,verbose_name='标题')
    roll_image=models.ImageField(upload_to='roll_image/',verbose_name='滚动图',max_length=200)
    url=models.URLField(max_length=200,verbose_name='访问地址')
    index=models.IntegerField(verbose_name='顺序',default=100)
    create_time=models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
        db_table='scroll_bar'
        verbose_name='滚动图'
