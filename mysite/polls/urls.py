# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 20:54
# @Author  : Tyrion
# @Email   : 1092196493@qq.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views


# app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

