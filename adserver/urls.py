from django.conf.urls import patterns, url

from adserver import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name = 'index'),
                       url(r'^int$', views.intent, name = 'intent'),
                       url(r'^conv', views.conversion, name = 'conversion'),
                       url(r'^clk', views.click, name = 'click'),)