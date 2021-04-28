from operator import*
a,b=10,20
print(gt(a,b))
print(mul(a,b))
print(mod(a,b))
print(concat("FACE","Prep"))
from decimal import*
a,b=10,3
c=a/b
print(c)
print(Decimal(c))
from random import*
print(randint(10,20))
list1=[30,23,45,16,89,56]
print(choice((list1)))
print(uniform(10,20))
# from string import*
# print(capwords("FACE prep"))
# print(ascii_letters)
# from math import*
# print(sqrt((16)))
# print(factorial(5))
# import math
# print("the value of pi is",math.pi)
# import math as m
# print("the value of pi is",m.pi)
# from math import pi, e
# pi
# 3.141592653589793
# e
# # 2.718281828459
# my_list=[1,2,3,5]
# print(my_list[2:3])
# print(my_list[:1])
# print(my_list[:-2])
# print(my_list[1:])
# my_list=['p','t','e','w','q']
# # print(my_list[0])
# # print(my_list[3])
# # print(my_list[4])
# # n_list=["happy",[2,5,8,5]]
# # print(n_list[1][2])
# # print(my_list[0][1])
# print(my_list[-1])
# print(my_list[-5])
# odd=[2,5,8,6,3]
# odd[0]=1
# print(odd)
# odd[1:4]=[7,0,9]
# print(odd)
# odd=[1,2,5]
# odd.append(7)
# print(odd)
# odd.extend([8,9,7,6,2])
# print(odd)
# odd.remove(2)
# print(odd)
# odd.reverse()
# print(odd)
#odd.count(odd)
#print(odd)
# odd.pop()
# print(odd)
# odd.insert(9,0)
# print(odd)
# odd.sort()
# print(odd)
# odd.index(odd)
# print(odd)
# odd.insert(2,64)
# print()
# # odd.seq()
# list=(12,51,45,21,96,7)
# tuple=tuple(list)
# print("tuple elements :",tuple)
# tuple1=('uytr','syt')
# tuple2=(457,'htguj')
# len(tuple2)
# print("lenght of tuple:",len(tuple2))
# max(tuple1)
# print("maximum value of tuple:",max(tuple1))
# min(tuple1)
# print("minimum value of tuple:",min(tuple1))
# print("Count for 457:",tuple2.count(457))
# print("Count for htguj:",tuple2.count('htgui'))
# #print("tuple2 :".tuple2.pop())
# tuple1.remove('uytr')
# # print("tuple1:",tuple1)
# var1='hello world!'
# var2="python programming"
# print("var1[0]:",var1[0])
# print("var2[1:5]",var2[1:5])
# print("updated string:-",var1[:6]+'python')
# print(u'hello ,world!')
# print(r'C:\\nowhere')
# print('C:\\nowhere')
# # print("my name is %s and weight is %d kg!"%('zara',457))
# default_order="{},{}and{}".format('john','Bill','sean')
# print('\n---Default order ---')
# print(default_order)
# positional_order="{1},{0} and {2}".format('john','Bill','sean')
# print("\n---positional order ---")
# print(positional_order)
# keyword_order="{s},{b} and {j}".format('j=john','b=Bill','s=Sean')
# # print('\n--- keyword order ---')
# # print(keyword_order)
# print("{:5d}".format(12345))
# print("{:2d}".format(1234))
# print("{:8.3f}".format(12.2346))
# print("{:05d}".format(12))
# print("{:08.3f}".format(12.2346))
# print("{:5d}".format(12))
# print("{:^10.3f}".format(12.2346))
# print("{:<05d}".format(12))
# print("{:=8.3f}".format(-12.2346))
# print("{:5}".format("cat"))
# print("{:>5}".format("cat"))
# print("{:^5}".format("cat"))
# print("{:*^5}".format("cat"))
# print("{:>05}".format("cat"))
# print("{:.3}".format("caterpillar"))
# print("{:5.3}".format("caterpillar"))
# print("{:^5.3}".format("caterpillar"))
# person={'age':23,'name':'adam'}
# # print("{p[name]}'s age is:{p[age]}".format(p=person))
# string="{:{fill}{align}{width}}"
# print(string.format('cat',fill='*',align='^',width='5'))
# num="{:{align}{width}.{precision}f}"
# # print(num.format(123.236,align='<',width=8,precision=2))
# import datetime
# date=datetime.datetime.now()
# print("it's now :{:%Y/%m/%d %H:%M:%S}".format(date))
# complexNumber=1+2j
# print("Real part:{0.real} and Imaginary part:{0.imag}".format(complexNumber))
# class person:
#     def _format_(self,format):
#         if(format =='age'):
#             return '23'
#         return 'None'
# #         print("Adam's age is:{:age}".format(Person()))
# print("Quotes: {0!r},without Quotes:{0!s}".format("cat"))
# class Person:
#     def _str_(self):
#         return "STR"
#     def __repr__(self):
#         return "RElPR"
# print("repr:{p!r},str:{p!s}".format(p=Person()))
# l=[1,2,3,4]
# l.reverse()
# print(l)
# l1=[1,2]
# l2=[3,4]
# l1=[l1,l2]
# print(l1)
# l=[1,2,3,4]
# print(l[:2],l[2:])
#
# a_list=[9,4,5,6,4,6,4,6,5]  #using for loop remove duplicates
# without_duplicates=[]
# for number in a_list:
#     if number not in without_duplicates:
#         without_duplicates.append(number)
# print(without_duplicates)
#n=int(input("Enter the value of 'n': "))  #fibonacci
# a=0
# b=1
# sum=0
# count=1
# print("Fibonacci series:",end=" ")
# while(count<=n):
#   print(sum,end =" ")
#   count+=1
# a=b
# b=sum
# sum=a + b
# x=0
# y=1
# fibo=0
# while fibo<10:
#     fibo=fibo+1
#     z=x+y
# print(z)
# x,y=y,z
def recur_fibo(n):
  if n <=1:
      return  n
  else:
    return(recur_fibo(n-1))+recur_fibo(n-2)
    nterms=10
  if nterms<=0:
    print("Plese enter a positive in integer")
  else:
      print("Fibonacci sequence:")
  for i in range(nterms):
        print(recur_fibo(i))


