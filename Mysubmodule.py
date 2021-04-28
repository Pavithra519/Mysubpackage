import re

n='pavitra123'
k=re.match('pavitra',n).group()
print (k)


c=re.search('vi',n).group()
print (c)
m=re.findall('a',n)
print (m)
##########################method=2#####################################
u=re.search('\d{3}',n).group()
print (u)
o=re.search('(?:a)',n).group()
print (o)
p=re.findall('i',n)
print(p)
###########################method=3####################################

y=re.match('[A-Z-a-z]{7}[0-9]{3}',n).group()
print (y)
a=re.search( '(?:a)',n).group()
print(a)