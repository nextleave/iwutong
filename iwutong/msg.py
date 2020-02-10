# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

WECHAT_TOKEN = 'Hello_Yuncong'
AppID = 'wx39a8f5372b61073a'


# AppSecret = 'a99bf714db26bc4ae2f53484513ca754'


@csrf_exempt
def index(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")
