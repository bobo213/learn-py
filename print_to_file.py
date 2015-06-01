str="a string to print to file"
f=open('out.txt','w')
print >>f,str
f=open('out.txt','r')
print f.read()
f.close()
