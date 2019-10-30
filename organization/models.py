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
    city = models.ForeignKey(City, verbose_name='所在城市',on_delete=models.CASCADE)

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
    org=models.ForeignKey(OrganInfo,verbose_name='所属机构',on_delete=models.CASCADE)

    class Meta:
        verbose_name='教师'
        db_table='teacher'
