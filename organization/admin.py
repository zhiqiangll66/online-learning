from django.contrib import admin

# Register your models here.
from .models import *

class CityAdmin(admin.ModelAdmin):
    list_display = ['name','describe','add_time']
    search_fields = ['name','describe']
    list_filter = ['name','describe','add_time']

admin.site.register(City,CityAdmin)


class OrganInfoAdmin(admin.ModelAdmin):
    list_display = ['name','describe','org_log','address','city','add_time']
    search_fields = ['name','describe','org_log','address','city']
    list_filter = ['name','describe','org_log','address','city','add_time']

admin.site.register(OrganInfo,OrganInfoAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','work_year','work_company','post','charact','org','add_time']
    search_fields = ['name','work_year','work_company','post','charact','org']
    list_filter = ['name','work_year','work_company','post','charact','org','add_time']

admin.site.register(Teacher,TeacherAdmin)


