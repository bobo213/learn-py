__author__ = 'liubo'

import socket

ip3 = raw_input("Enter IP:")

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print hostname
ipList = socket.gethostbyname_ex(hostname)
#print ipList
print ip3
ip1='1.2.3.4'
ip2='2.3.4.5'

if (ip3 == ip1):
    print ("ok")
    print ip1
else:
    print cmp(ip1,ip3)
