# -*- coding:utf-8 -*-
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^tasks/$', views.task_list, name='task_list'),
    # url(r'^tasks/$', views.TaskList.as_view(), name='task_list'),
    # url(r'^tasks/$', views.TaskListCreate.as_view(), name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
]