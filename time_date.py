__author__ = 'liubo'
import calendar

cal = calendar.month(2015, 1)


import time;



print "time.time(): %f " %  time.time()
print time.localtime( time.time() )
print time.asctime( time.localtime(time.time()) )

print time.strftime("%Y-%m-%d-%A %X", time.localtime())

print time.strftime('%Y/%m/%d %H-%M-%S',time.localtime())