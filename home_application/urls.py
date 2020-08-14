# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    # 主页相关
    (r'^$', 'home'),
    (r'^login_info$', 'login_info'),

)
