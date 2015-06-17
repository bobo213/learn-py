__author__ = 'liubo'
#encoding:UTF-8
import urllib
url =  "http://www.baidu.com"
data = urllib.urlopen(url).read()
urllib.urlopen("http://www.baidu.com")
data = data.decode('UTF-8')
print(data)