# -*- coding:utf-8 -*-
from django.conf.urls import url ,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users' ,views.UserViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
]

# urlpatterns = format_suffix_patterns([
#     url(r'^$',views.api_root),
#
#     url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
#     # url(r'^tasks/$', views.TaskList.as_view(), name='task_list'),
#     # url(r'^tasks/$', views.TaskListCreate.as_view(), name='task_list'),
#     url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view(), name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(),name='snippet-highlight'),
#
#     url(r'^users/$',views.UserList.as_view() ,name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view() ,name='user-detail'),
#
# ])

# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#     namespace='rest_framework')),
# ]