# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-10-28 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=300, verbose_name='评论')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='用户')),
            ],
            options={
                'verbose_name': '课程评论',
                'db_table': 'course_comment',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机')),
                ('course_name', models.CharField(max_length=30, verbose_name='课程名称')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户咨询',
                'db_table': 'user_ask',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户课程',
                'db_table': 'user_course',
            },
        ),
        migrations.CreateModel(
            name='UserMessg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='接收用户')),
                ('messg', models.CharField(max_length=300, verbose_name='消息内容')),
                ('has_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户消息',
                'db_table': 'user_messg',
            },
        ),
        migrations.CreateModel(
            name='UserStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField(default=0, verbose_name='数据id')),
                ('store_type', models.IntegerField(choices=[(1, '课程'), (2, '课程机构'), (3, '教师')], default=1, verbose_name='收藏')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏',
                'db_table': 'user_store',
            },
        ),
    ]
