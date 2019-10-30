"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
#自带专门处理静态文件的

from users.views import login


# import xadmin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^xadmin/', xadmin.site.urls),
    url('^$',TemplateView.as_view(template_name='index.html'),name='index'),
    # url('^login/$',TemplateView.as_view(template_name='login.html'),name='login'),
    url('^login/$',login,name='login'),


]