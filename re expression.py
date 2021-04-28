import re
s='kavitha'
j=re.match('ka*v',s).group()
print(j)
f=re.search('tha',s).group()
print(f)
h=re.findall('k|a',s)
print(h)
o=re.subn('\s+','',s)
print(s)
#u=re.compile('kav',s).gruop()
#print(u)
k='abg@gmail.com'
l=re.match('[A-Z-a-z]{3}\@[A-Z-a-z]{5}\.[A-Z-a-z]{3}',k).group()
print(l)

l='192.168.1.1'
import re
c=re.match ('\d{3}.\d{3}.\d{1}.\d{1}',l).group()
print (c)
h='Test log is one of the crucial test artifact prepared during the process of testing. ' \
'It provides a detailed summary of the overall test run and indicates the passed and ' \
'failed tests. Additionally, test log also contains details and information about various test operations, ' \
'including the source of issues and the reasons for failed operations. The focus of this report/document is to ' \
'enable post execution'
d=re.findall('log',h)
f=re.findall('test',h)
print(f)
print(d)
H='pavinuthana@gmail.com'
j=re.match('[A-Z-a-z]{11}@[A-Z-a-z]{5}.[A-Z-a-z]{3}',H).group()
g=re.match('\w+@\w+.\w+',H).group()
#k=re.search('^p.........a$',k).group()
#print(k)
print(j)
print(g)
p="Your IP address	59.98.131.96   Your IP address	59.98.131.96	Your IP address	220.198.131.96    Your IP address	225.98.133.96	City	Organization	BSNL"
k=re.findall('\d+.\d+.\d+.\d+',p)
print(k)
import uuid
import re
j='ip:A0-7B-A5-A7-G9-6E ip:A0-7B-A5-A7-G9-6E ip:A0-7B-A5-A7-G9-6E ip:A0-7B-A5-A7-G9-6E'
c=re.match('(?:ip:[A-G]{1}\d{1}-\d{1}[A-G]-[A-G]{1}\d{1}-[A-G]{1}\d{1}-[A-G]{1}\d{1}-\d{1}[A-G])',j).group()
a=re.findall('(?:ip:[A-G]{1}\d{1}-\d{1}[A-G]-[A-G]{1}\d{1}-[A-G]{1}\d{1}-[A-G]{1}\d{1}-\d{1}[A-G])',j)
print (a)
print(c)

s='paviras132442543554436643'
for i in s:
    c=0
     #c+=1
c=c+1
print (c)
s='ip:234.45.67.3 ip:203-517-74-9 ip:77.67.6.8'

p=re.findall('(?:ip:\d{3}.\d{2}.\d{2}.\d{1}\s\d{3}\d{3}\d{2}\d{1}\s\d{2}.\d{2].\d{1}.\d{1})',s)
#             # '[A-Z]{1}\d{1}-\d{1}[A-Z]{1}'
#             # '\d{2}.\d{2}.\d{1}.\d{1})',s).group()
#
#print(p)
# j="abc@gmail.com abc@yahoo.com abc@rcut.com abc@gmail.com"
# h=re.findall('abc@gmail.com|abc@gmail.com',j)
# print(h)
# c="8074493335 9533678196 9003980982 8074493335"
# r=re.findall('8074493335|8074493335',c)
# print(r)

# s="{'r':1,'a':2,'y':3,'a':4,'v':5,'a':6,'r':7,'a':8,'m':9}"
# Dict=eval(s)
# print(Dict)
# print(Dict['r'])
# print(Dict['y'])
# s="pavithra"[::-1]  #reverse
# print(s)
def reverse(text):
    a = ""
    for i in range(1,len(text)+1):
        a +=text[len(text)-i]
        return a
print(reverse("Hello world"))
# # word="haritha"  #using for loop lenght
# # for letter in word:
# #      print(len(word))
#      #or
# def findeLen(s):
#  counter = 0
#  for i in s:
#      counter += 1
#      return counter
# s="geeks"
# print(findeLen(s))
# d='ip:234.45.67.3 ip:203-517-74-9 ip:77.67.6.8'
# P=re.match('(?:ip:/d{3}./d{2}./d{2}./d{1}/s/d{3}-/d{3}-/d{2}-/d{1}/s/d{2}./d{2}./d{1}./d{1})').group()
#print(P)
w='npna@gmail.com  jku@iphone.com   huy@yaoo.com  kai@gmail.com'
y=re.findall('[A-Z-a-z]{4}\@[A-Z-a-z]{5}\.[A-Z-a-z]{3}',w)
print(y)
t=re.match('[com]',w).group()
print(t)













