__author__ = 'liubo'

import os
ip = os.popen("ifconfig en0|grep 'inet'|awk '{print $2}'|awk NR==2").read()
internetip = os.popen("curl -s ifconfig.me").read()
print ip
print internetip

f=open('ip2.txt','r')
print f.read()
f.close()
print "-------"
f=open('ip2.txt','w')
#f.truncate()
f.write(str(internetip)+'\n')
#print f.read()
print "-------"
f.close

print "filename:", f.name
f=open('ip2.txt','r')
print "code:",f.read()
print "open?or closed?:",f.closed
