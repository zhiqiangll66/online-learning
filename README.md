# online-learning
在线学习
# 基于admin搭建Django网站学习系后台管理系统

## 内容

```
开发环境的搭建；
数据库设计及admin搭建后台管理系统
系统功能模块的实现
web系统知识及网络安全
admin扩展
```

## virtualenv虚拟环境

virtualenv优点：

```
使得不同应用开发环境相互独立
环境升级不影响其他应用，也不会影响全局的python环境
它防止系统中出现包管理混乱和版本的冲突．
方法一：
安装：pip install virtualenv
virtualenv liu 虚拟环境命名．
cd liu #进入虚拟环境
cd Scripts #进入虚拟激活文件夹(win系统)
cd bin #进入虚拟激活文件夹(linux系统)
activate.bat #激活虚拟环境(win系统)
source activate #激活虚拟环境(linux系统)
pip3 list #查看本虚拟机有什么运用软件
(liu)tarena@tarena:~/liuzhiqiang/month04/liu/bin$ pip install requests#虚拟环境里安装运用
deactivate.bat #退出虚拟环境(win系统)
deactivate #退出虚拟环境(linux系统)

方法二：
pip install virtualenvwrapper-win(win操作需要-win)
mkvirtualenv testvir2
deactivate #退出虚拟环境
workon testvir2 #进入这个虚拟环境
pip install requests #安装安装包　
```

## 开发环境的搭建

```
pip install virtualenv
virtualenv liu 
cd liu 
cd bin
source activate
(liu)tarena@tarena:~/liuzhiqiang/month04/liu/bin$　pip3 list 
(liu)tarena@tarena:~/liuzhiqiang/month04/liu/bin$　pip install requests
(liu)tarena@tarena:~/liuzhiqiang/month04/liu/bin$　pip3 install django==1.9
(liu) tarena@tarena:~/liuzhiqiang/month04/liu/bin$ django-admin startproject study
(liu) tarena@tarena:~/liuzhiqiang/month04/liu/bin$ pip install pymysql
(liu) tarena@tarena:~/liuzhiqiang/month04/liu/bin/study$ pip3 install django-simpleui
＃搭建　admin 页面主题．
环境搭建完毕
```

## Ｄjango的设计与开发是基于app的

步骤：根据需求设计django app，再根据各个app设计对应的数据库即各app models设计，再数据表生成修改

需求：设计在线教育平台，此平台可以由各个授课机构（包括本机构，其他机构如高校等）提供课程，授课机构让自己机构的老师录制教育视频上传到本平台中，学员通过本平台完成在线学习．

## django app设计:　

```
users-用户管理：功能：对用户进行管理，如用户的收藏及基本信息．
course-课程管理：功能：课程基本信息．
organization-机构和教师管理：因为教师属于结构．
operation-用户操作管理：功能：记录用户操作信息．
```

## users app 创建：

１．创建后台服务文件夹：

```
django-admin startproject learning_system
python3 manage.py runserver
```

２．创建users app 文件包目录

```
python3 manage.py startapp users
```

３．连接mysql数据库：在 learning_system父文件夹下的 learning_system子文件夹下__init__.py文件中：

```
import pymysql
pymysql.install_as_MySQLdb()
```

４．在 learning_system父文件夹下的 learning_system子文件夹下settings.py文件中：

```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
改为如下：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'learn',
        'USER':'root',
        'PASSWORD':'123456',xadmin搭建后台管理系统
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}

INSTALLED_APPS = [
    'simpleui',#导入admin后台主题　
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'course',
    'organization',
    'operation',
]
```

５．在users文件夹下的models.py文件创建数据库表格：

```python
from django.db import models

# Create your models here.
#表名：users_userprofile
#库名：learn
class UserProfile(models.Model):
    nickname=models.CharField(max_length=20,verbose_name='昵称',default='')
    birthday=models.DateField(max_length=30,verbose_name='生日',default='')
    gusers app 创建：ender=models.CharField(max_length=10,choices=(('male','男'),('female','女')),default='female')
    address=models.CharField(max_length=50,verbose_name='区域',default='')
    phone=models.CharField(max_length=11,verbose_name='手机',null=True,blank=True)
    #null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空，那么在新建一个model对象的时候是不会报错的！！
    #blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
    email=models.EmailField(max_length=30,verbose_name='邮箱')
    name=models.CharField(max_length=20,verbose_name='姓名',primary_key=True)
    head_image=models.ImageField(upload_to='head_image/',null=True)
    login_time=models.DateTimeField('登入时间',auto_now=True)

class Meta:chil
    db_table = 'users_userprofile'
    verbose_name = '用户信息'

#表名：email_verify_record
#库名：learn
class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=30,verbose_name='邮箱验证码')
    send_type=models.CharField(max_length=20,choices=(('forget','找回密码'),('register','注册')))
    send_time=models.DateTimeField('发送验证时间',auto_now=True)

class Meta:
    db_table = 'email_verify_record'
    verbose_name = '邮箱验证'

#表名：scroll_bar
#库名：learn
class Scrollbar(models.Model):
    title=models.CharField(max_length=100,verbose_name='标题')
    roll_image=models.ImageField(upload_to='roll_image/',verbose_name='滚动图',max_length=200)
    url=models.URLField(max_length=200,verbose_name='访问地址')
    index=models.IntegerField(verbose_name='顺序',default=100)
    create_time=models.DateTimeField('创建时间',auto_now_add=True)

class Meta:
    db_table='scroll_bar'
    verbose_name='滚动图'

终端运行如下命令来格式化表格：
python3 manage.py makemigrations
python3 manage.py migrate
```

![](/home/tarena/桌面/网站学习系统/2019-10-29 13-21-24屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-24 13-10-47屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-24 13-11-26屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-23 20-53-09屏幕截图.png)

## course app 创建：

１．创建course app 文件包目录

```
python3 manage.py startapp course
```

分析：

```
课程自身需要用一张表存储
课程基本信息需要一张表格course
一个课程有多个章节，属于一对多关系，因而需要建立章节表lesson
一个章节可以有多个视频，属于一对多关系，因为需建立视频表video
一个课程可以有多个下载地址，属于一对多关系，需建立课程资源表course_resource
```

２．在course文件夹下的models.py文件创建数据库表格：

```python
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
    course=models.ForeignKey(Course,verbose_name='课程')
    #与课程一对多关系，通过外键进行映射
    name=models.CharField(verbose_name='章节',max_length=200)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

class Meta:
    verbose_name='章节'
    db_table='lesson'

class Video(models.Model):
    lesson=models.ForeignKey(Lesson,verbose_name='章节')
    name=models.CharField(verbose_name='视频',max_length=300)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

class Meta:
    verbose_name='视频'
    db_table='video'

class CourseResource(models.Model):
    course=models.ForeignKey(Course,verbose_name='课程')
    name=models.CharField(max_length=300,verbose_name='名称')
    download=models.FileField(verbose_name='下载地址',upload_to='course_resource/',null=True)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

class Meta:
    verbose_name='下载地址'
    db_table='course_resource'
    
终端运行如下命令来格式化表格：
python3 manage.py makemigrations
python3 manage.py migrate
```

![](/home/tarena/桌面/网站学习系统/2019-10-25 15-17-40屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-25 15-17-19屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-25 15-16-51屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-25 15-16-14屏幕截图.png)

## organization app 创建：

１．创建organization app 文件包目录

```
python3 manage.py startapp organization
```

分析：

```
课程机构基本信息表organ_info
课程数目，学习人数是动态的，机构地址，机构介绍（机构课程，机构老师可通过外键获取），机构收藏数，点击数
结构的教师的基本信息表
城市基本信息表
```

２．在organization文件夹下的models.py文件创建数据库表格：

```python
from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(verbose_name='城市名',max_length=30)
    describe=models.TextField(verbose_name='城市描述')
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now_add=True)

class Meta:
    verbose_name='城市'
    db_table='city'

class OrganInfo(models.Model):
    name=models.CharField(verbose_name='机构名称',max_length=100)
    describe=models.TextField(verbose_name='机构描述')
    click_num=models.IntegerField(verbose_name='点击数',default=0)
    store_num=models.IntegerField(verbose_name='收藏数',default=0)
    org_log=models.ImageField(verbose_name='机构log',upload_to='org_log/',null=True)
    address=models.CharField(verbose_name='机构地址',max_length=200)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    city = models.ForeignKey(City, verbose_name='所在城市')

class Meta:
    verbose_name='课程信息'
    db_table='organ_info'

class Teacher(models.Model):
    name=models.CharField(verbose_name='教师名称',max_length=30)
    work_year=models.IntegerField(verbose_name='工作年限')
    work_company=models.CharField(verbose_name='工作公司',max_length=30)
    post=models.CharField(verbose_name='职务',max_length=30)
    charact=models.CharField(verbose_name='教学特点',max_length=30)
    click_num = models.IntegerField(verbose_name='点击数', default=0)
    store_num = models.IntegerField(verbose_name='收藏数', default=0)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    org=models.ForeignKey(OrganInfo,verbose_name='所属机构')

class Meta:
    verbose_name='教师'
    db_table='teacher'
    
终端运行如下命令来格式化表格：
python3 manage.py makemigrations
python3 manage.py migrate
```

![](/home/tarena/桌面/网站学习系统/2019-10-25 19-47-10屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-25 19-46-30屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-25 19-46-05屏幕截图.png)

## operation app 创建：用户相关操作

１．创建operation  app 文件包目录

```
python3 manage.py startapp operation
```

分析：

```
用户咨询表：user_ask
用户对课程的评论表：course_comment
用户收藏表：user_store
用户消息表：user_message
用户学习的课程表：user_course
```

２．在operation文件夹下的models.py文件创建数据库表格：

```python
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
    user=models.ForeignKey(UserProfile,verbose_name='用户')
    course=models.ForeignKey(Course,verbose_name='课程')
    comments=models.CharField(verbose_name='评论',max_length=300)
    add_time=models.DateTimeField(verbose_name='添加时间',auto_now=True)

class Meta:
    verbose_name='课程评论'
    db_table='course_comment'


class UserStore(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
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
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now=True)

class Meta:
    verbose_name='用户课程'
    db_table='user_course'
    
终端运行如下命令来格式化表格：
python3 manage.py makemigrations
python3 manage.py migrate
```

![](/home/tarena/桌面/网站学习系统/2019-10-25 20-45-13屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-25 20-44-56屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-25 20-44-39屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-25 20-44-16屏幕截图.png)

![](/home/tarena/桌面/网站学习系统/2019-10-25 20-43-55屏幕截图.png)

## admin搭建后台管理系统

### 后台系统特点

```
权限管理－－后台管理必不可少
少前端样式－－后台管理的首要解决问题是快速搭建，因而少前端样式
快速开发－－django后台系统django的admin是全自动后台管理系统，非常智能．它从模型中读取元数据，以提供一个快速的，以模型为中心的界面，
实际上django的admin也是一个app，是搭建项目时自动生成的．
http://127.0.0.1:8000/admin　进入django的admin.
```

### １．创建 admin　的账号及登入密码

```python
终端运行如下程序，创建 admin 的账号和密码等．
$ python3 manage.py createsuperuser
Username (leave blank to use 'tarena'): liuzhiqiang
Email address: zhiqiangll66@163.com
Password:
Password (again): 
Superuser created successfully.
$ python3 manage.py runserver
```

### ２．注册各 app 的admin

```python
注册 users app 的 admin，在在users文件夹下的admin.py文件注册其对应admin：

from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(UserProfile)

class EmailVerifyRecordAdmin(admin.ModelAdmin):
    #为邮箱验证的后台管理界面添加便于操作的新功能。
    list_display =['code','send_type','send_time','email']
    # 去控制哪些字段会显示在Admin的修改列表⻚面中。
    search_fields = ['code','send_type','email']
    #设置启用 Admin 更改列表⻚面上的搜索框。
    list_filter = ['code','send_type','send_time','email']
    #设置激活 Admin 修改列表⻚面右侧栏中的过滤器即通过字段筛选功能

admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)

class ScrollbarAdmin(admin.ModelAdmin):
    # 为滚动图的后台管理界面添加便于操作的新功能。
    list_display = ['title', 'roll_image', 'url', 'index','create_time']
    # 去控制哪些字段会显示在Admin的修改列表⻚面中。
    search_fields = ['title', 'roll_image', 'url', 'index']
    # 设置启用 Admin 更改列表⻚面上的搜索框。
    list_filter = ['title', 'roll_image', 'url', 'index','create_time']
    # 设置激活 Admin 修改列表⻚面右侧栏中的过滤器即通过字段筛选功能

admin.site.register(Scrollbar,ScrollbarAdmin)

admin.site.site_header='教学管理系统' #修改页面主题
admin.site.site_title='教学管理系统'　#修改页面主题　

其他各 app 注册类推．
```

### ３．admin搭建后台管理系统

```
pip3 install xadmin 　下载安装　xadmin
```

## 与前端交互设计

```
在settings.py内加载前端 html 的路径．
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
改为如下：
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
给静态文件 static 内的　css,image,js文件等添加路径
STATICFILES_DIRS=[(
    os.path.join(BASE_DIR,"static")
)]
```
