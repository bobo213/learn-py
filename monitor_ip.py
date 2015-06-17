#!/usr/bin/python
#-*- coding: UTF-8 -*-
#监控本服务器公网ip，如果ip变化则发邮件
# 将现有公网ip写入到 ip_old.txt中
#import os
import smtplib
from email.MIMEText import MIMEText
#from email.Utils import formatdate
from email.Header import Header
#import sys
import time;
import os

#内网ip
#ip = os.popen("ifconfig en0|grep 'inet'|awk '{print $2}'|awk NR==2").read()
#print "内网ip:",ip

#邮件配置
sender = 'iknowing@163.com'
receiver = 'liubo@vbuluo.com'
subject = 'Python email test'
smtpserver = 'smtp.163.com'
username = 'iknowing@163.com'
password = '61659660'

# 时间戳
tet = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())

'''通过shell获取公网IP地址 赋值给 internetip'''
internetip = os.popen("curl -s ifconfig.me").read()

#读取文本文件 内容 赋值到ip_old 为老的ip地址
f2 = open('/home/liubo/py/ip_old.txt','r')
ip_old = f2.readline()
f2.close()
#新地址和老地址对比，如果相同则 不变 不发邮件
if  ip_old == internetip :
    print("IP not changed")
    #f=open('out.txt','w')
   #print >>f,str

#如果地址不一样 则发邮件
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
#更新ip_old.txt文件 下次做对比
    ip_old=open('/home/liubo/py/ip_old.txt','w')
    ip_old.write(str(internetip)+'\n')
    print "-------"
    ip_old.close()

#写入检测的时间戳
    str="ip更换时间"
    print(str)
#用append模式打开文件 执行插入
    fs=open('/home/liubo/py/out.txt','a')
    #print >>fs,str+tet
    fs.write(internetip+" "+tet+"\n")
    fs.close()

