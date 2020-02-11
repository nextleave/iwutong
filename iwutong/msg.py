# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import requests
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wechatpy import parse_message, create_reply

WECHAT_TOKEN = 'Hello_Yuncong'
AppID = 'wx39a8f5372b61073a'


# AppSecret = 'a99bf714db26bc4ae2f53484513ca754'


@csrf_exempt
def index(request):
    signature = request.GET.get('signature', '')
    timestamp = request.GET.get('timestamp', '')
    nonce = request.GET.get('nonce', '')
    encrypt_type = request.GET.get('encrypt_type', 'raw')
    msg_signature = request.GET.get('msg_signature', '')
    if request.method == 'GET':
        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")

    # POST request
    if encrypt_type == 'raw':
        # plaintext mode
        print(request.body)

        msg = parse_message(request.body)
        if msg.type == 'text':
            reply = talk(msg.content.strip())
        else:
            reply = create_reply('Sorry, can not handle this for now', msg)
        return HttpResponse(
            reply, content_type="text/plain")


def talk(content):
    url = 'http://www.tuling123.com/openapi/api'
    s = requests.session()
    d = {'key': 'b3f333bc09674b8986360293916bf84e', 'info': content}
    data = json.dumps(d)
    r = s.post(url, data=data)
    text = json.loads(r.text)
    return text['text']
