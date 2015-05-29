__author__ = 'liubo'
#coding:utf-8
import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email.Header import Header
import sys
import time;
import os

sender = 'iknowing@163.com'
receiver = 'liubo@vbuluo.com'
subject = 'Python email test'
smtpserver = 'smtp.163.com'
username = 'iknowing@163.com'
password = '61659660'
tet = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
internetip = os.popen("curl -s ifconfig.me").read()

message = 'I send a message by Python.测试' + ',时间' +tet+ ',公网IP地址为：' +internetip
msg = MIMEText(message)
msg['Subject'] = Header(subject+ tet, 'utf-8')
print msg
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
print "发送成功"
smtp.quit()

