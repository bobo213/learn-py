__author__ = 'Administrator'
# -*- coding: utf-8 -*-
# 监控本机的公网ip，如果ip有变化则发邮件
import os
import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email.Header import Header
import sys
import time;
import os

'''获取IP地址'''
#ip = os.popen("ifconfig en0|grep 'inet'|awk '{print $2}'|awk NR==2").read()
#print "内网ip:",ip
#print "公网ip:",internetip

sender = '----@163.com'
receiver = '******'
subject = 'Python email test'
smtpserver = 'smtp.163.com'
username = '-----@163.com'
password = '******'
tet = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
internetip = os.popen("curl -s ifconfig.me").read()
#print ip_old.read()
#print "ip_old=",(ip_old.read())
#print "internetip=",(internetip)
 
f2 = open('ip_old.txt','r')
ip_old = f2.readline()
f2.close()

if  ip_old == internetip :
    print("IP not changed")
else:
    print("ip changed!!!")
    message = 'ip changed!' + ',时间' +tet+ ',公网IP地址为：' +internetip
    msg = MIMEText(message)
    msg['Subject'] = Header(subject+ tet, 'utf-8')
    print msg
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    print "发送成功"
    smtp.quit()
    ip_old=open('ip_old.txt','w')
    ip_old.write(str(internetip)+'\n')
    print "-------"
    ip_old.close
