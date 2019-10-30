from django.contrib import admin

# Register your models here.

from .models import *

class UserAskAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','course_name','add_time']
    search_fields = ['name','mobile','course_name']
    list_filter = ['name','mobile','course_name','add_time']

admin.site.register(UserAsk,UserAskAdmin)


class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ['user','course','comments','add_time']
    search_fields = ['user','course','comments']
    list_filter = ['user','course','comments','add_time']

admin.site.register(CourseComment,CourseCommentAdmin)


class UserStoreAdmin(admin.ModelAdmin):
    list_display = ['user','course','store_id','store_type','add_time']
    search_fields = ['user','course','store_id','store_type']
    list_filter = ['user','course','store_id','store_type','add_time']

admin.site.register(UserStore,UserStoreAdmin)


class UserMessgAdmin(admin.ModelAdmin):
    list_display = ['user','messg','has_read','add_time']
    search_fields = ['user','messg','has_read']
    list_filter = ['user','messg','has_read','add_time']

admin.site.register(UserMessg,UserMessgAdmin)


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user','course','add_time']
    search_fields = ['user','course','add_time']
    list_filter = ['user','course']

admin.site.register(UserCourse,UserCourseAdmin)