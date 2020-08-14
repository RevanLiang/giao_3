# -*- coding: utf-8 -*-
import sys

from common.mymako import render_mako_context, render_json
from conf.default import *

reload(sys)
sys.setdefaultencoding('utf8')

# 通用成功返回
SUCCESS_RETURN_DICT = {"result": True, "data": "success"}


def home(request):
    return render_mako_context(request, '/index.html')


def login_info(request):
    resp = render_json({
        "result": True,
        "data": {
            "username": request.user.username,
            "logout_url": LOGOUT_URL,
            "super": request.user.is_superuser
        }})
    from django.core.context_processors import csrf
    resp.set_cookie('cwcsrftoken', csrf(request)['csrf_token'])
    return resp
