#!/usr/bin/python
#__author__ = 'liubo'
# coding= utf8
import os
import time
#要备份的目录列表
source = ['/Users/liubo/PycharmProjects/learn-py','/Users/liubo/Public']

#备份文件存放目录

target_dir = '/Users/liubo/backup/'

#文件名
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

#zip 命令%s 调用 str函数打印字符串,str函数返回原始字符串
zip_command = "zip -qr '%s' %s" % (target,' ' .join(source))

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup Failed'