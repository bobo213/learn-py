__author__ = 'Administrator'
import time;
import os;
f = open('C:/Users/Administrator/learn-py/test.txt','r')
print f.read()
f.close()
print time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
wtime = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
print wtime
f = open('C:/Users/Administrator/learn-py/test.txt','w')
f.write('wtime.as_string()')
f.close()

