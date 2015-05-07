"""{{ project_name }} URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from app_name import views

urlpatterns = (
    url(r'^$', views.api_root, name='api_root'),

    url(r'^api-token-auth/$', obtain_auth_token, name='api-token'),

    url(r'^api/placeholders/$', views.SprintList.as_view(), name='placeholder-list'),
    url(r'^api/placeholders/(?P<pk>[0-9]+)/$', views.SprintDetail.as_view(), name='placeholder-detail'),

    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)