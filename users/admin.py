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

admin.site.site_header='教学管理系统'
admin.site.site_title='教学管理系统'