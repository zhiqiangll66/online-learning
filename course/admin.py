from django.contrib import admin

# Register your models here.

from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','info','detail','difficulty','learning_times','students']
    search_fields = ['name','info','detail','difficulty','students']
    list_filter = ['name','info','detail','difficulty','learning_times','students']

admin.site.register(Course,CourseAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name','add_time']

admin.site.register(Lesson,LessonAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']

admin.site.register(Video,VideoAdmin)


class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ['course','name','add_time','download']
    search_fields = ['course','name','download']
    list_filter = ['course','name','add_time','download']

admin.site.register(CourseResource,CourseResourceAdmin)