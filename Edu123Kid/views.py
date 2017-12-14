# -*- coding: utf-8 -*-
from django.http import HttpResponse

import os
import sys
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
import json
from vaptchasdk import vaptcha
from aliyunsdkcore.profile import region_provider

REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"
ACCESS_KEY_ID = "LTAIoCLozjN0IYoH"
ACCESS_KEY_SECRET = "kfxePATQzmvNPSxMIDRuUc8VeKTraA"

vid, key = '5a1b8675a485fe214ce06f63', '5c8253b6c0c74f708c998d64789d1b66'
work_dir = os.path.dirname(os.path.abspath(__file__))
_vaptcha = vaptcha(vid, key)

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME,REGION,DOMAIN)

def get_vaptcha(request):
    html = [_vaptcha.get_challenge().encode('utf-8')]
    return HttpResponse(html)

def validate(request):
    result = _vaptcha.validate(challenge, token)
    if(result):
        return ['{"msg":"success"}'.encode('utf-8')]
    else:
        return ['{"msg":"fail"}'.encode('utf-8')]

def test(request):
    if request.method == 'POST':
        html = ""
        if request.POST.get('register'):
            html = request.POST['register']
        if request.POST.get('get-verification-code'):
            __business_id = uuid.uuid1()
            params = "{\"code\":\"888888\",\"product\":\"云通信\"}"
            html = send_sms(__business_id, request.POST['phone-number'], "越读悦写", "SMS_112465062", params)
    else:
        html = request.Get['q']
    return HttpResponse(html)


def send_sms(business_id, phone_numbers, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)
    # 短信模板变量参数
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)
    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)
    # 短信签名
    smsRequest.set_SignName(sign_name);
    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)
    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)
    # TODO 业务处理
    return smsResponse
