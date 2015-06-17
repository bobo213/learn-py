__author__ = 'liubo'

import time;
import os

internetip = os.popen("curl -s ifconfig.me").read()
tet = time.strftime('%Y/%m/%d %H-%M-%S',time.localtime())


c1 = 123456
f = open('ip2.txt','a')
f.write(str(c1)+internetip+" "+tet+"\n")
f=open('ip2.txt','r')
print f.read()
f.closed


