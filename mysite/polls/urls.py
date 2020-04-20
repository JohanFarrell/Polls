# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 20:54
# @Author  : Tyrion
# @Email   : 1092196493@qq.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

