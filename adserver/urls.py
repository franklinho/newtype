from django.conf.urls import patterns, url

from adserver import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name = 'index'),
                       url(r'^int$', views.detail, name = 'detail'),)