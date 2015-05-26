__author__ = 'liubo'
# coding= utf8
import re

text = "JGood is a handsome boy,he is cool,clever,and so on 123 ..."
regex = re.compile(r'\w*oo\w')
#查找所有包含'oo'的单词
print regex.findall(text)
regex_data = re.compile(r'\d{1,3}')
print regex_data.findall(text)
