# -*- coding: utf-8 -*-
import itchat
from itchat.content import *

#@itchat.msg_register(itchat.content.TEXT)
    #def text_reply(msg):
    #print msg.fromUserName + ':' + msg.text
#return  u'[憨笑]'

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('您好！')

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    return u'收到文件:%s' % (msg.fileName)

itchat.auto_login()
itchat.run()
