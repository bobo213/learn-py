# -*- coding: utf-8 -*-
#-*- coding:gbk -*-
import urllib2,re
import os
ip = os.popen("ifconfig en0|grep 'inet'|awk '{print $2}'|awk NR==2").read()

internetip = os.popen("curl -s ifconfig.me").read()
print "内网ip:",ip
print "公网ip:",internetip

