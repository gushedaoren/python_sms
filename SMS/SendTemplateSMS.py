#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-
from django.http import HttpResponse

from CCPRestSDK import REST
from rest_framework import generics
import ConfigParser

#���ʺ�
accountSid= '�������ʺ�';

#���ʺ�Token
accountToken= '�������ʺ�Token';

#Ӧ��Id
appId='����Ӧ��ID';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='sandboxapp.cloopen.com';

#����˿� 
serverPort='8883';

#REST�汾��
softVersion='2013-12-26';

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id

def sendTemplateSMS(request):


    to="13761398648"
    datas=""
    tempId=1

    #��ʼ��REST SDK
    rest = REST(serverIP,serverPort,softVersion)
    rest.setAccount(accountSid,accountToken)
    rest.setAppId(appId)
    
    result = rest.sendTemplateSMS(to,datas,tempId)
    for k,v in result.iteritems(): 
        
        if k=='templateSMS' :
                for k,s in v.iteritems(): 
                    print '%s:%s' % (k, s)
                    HttpResponse('{%s:%s}' % (k, s))
        else:
            print '%s:%s' % (k, v)
            return HttpResponse('{%s:%s}' % (k, v));
    
   
#sendTemplateSMS(�ֻ�����,��������,ģ��Id)