# coding= utf8
__author__ = 'liubo'


while True:
    s = raw_input('input something :')
    if s == 'quit':
        break
    if len(s) < 3:
        print 'Length of the string is', len(s),'继续'
        continue
    print '输入太多'