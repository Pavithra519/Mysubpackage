# # # class Parrot:
# # #     species ="brid" #class attribute
# # # def _init_(self,name,age): #instance attribute
# # #   self.name=name
# # #   self.age=age
# # #   blu=Parrot("Blu",10) #access the Parrot class
# # #   woo=Parrot("woo",15)
# # #   print("Blu is a {}".format((blu.__class__.species))) # class attribute
# # #   print("woo is also a {}".format(woo.__class__.species))
# # #   print("{} is {} years old".format(blu.name,blu.age)) # instance attribute
# # #   print("{} is{} years old".format(woo.name,woo.age))
# # class parrot:
# #   def __init__(self,name,age):
# #     self.name=name
# #     self.age=age
# #     def sing(self,song):
# #       return "{} sings {} ".format(self.name,song)
# #     def dance(self):
# #       return "{} is now dancing".format(self.name,dance)
# #     def acting(self):
# #       return "{} is now acting".format(self.name,acting)
# #     blu=parrot("Blu,10")
# #     print(blu.sing("Happy"))
# #     print(blu.dance())
# #     print(blu.acting())
# #inhiritance
#
# class A:
#   def add(self,a,b):
#     print (a+b)
# class B(A):
#   def sub (self,a,b):
#     print (a-b)
# g=B()
# g.add(10,20)
# g.sub(30,20)
# #inhiritance
# class Person:
#   def __init__(self, fname, lname):
#     self.lastname = lname
#     self.fristname = fname
#     pass                # pass is aplicable both classes,only function is pass
#
# class Student(Person):
#
#
#  def printname(self):
#   print(self.lastname, self.fristname)
#
# x = Student("Mike", "Olsen")
# x.printname()
# #super() using u dont have print element it is taken autometical
# class Person:
#   def __init__(self,fname,lname,year):
#      self.fristname=fname
#      self.lastname=lname
#   def printname(self):
#        print(self.fristname,self.lastname)
# class student(Person):
#     def printname(self,fname,lname,year):
#       super().__init__(fname, lname)
#       self.graduationyear = year
#
# x =student("Mike","Olsen",2019)
# print(x.graduationyear)
#class A:
#   def __int__(self,fname,lname):
#      self.fristname=fname
#      self.lastname=lname
#   def printname(self):
#      print(self.fristname,self.lastname)
# class B(A):
#   def __init__(self,fname,lname,year):
#       super().__init__(fname, lname)
#       self.graduationyear=year
#   def hello(self):
#     print("hello",self.fristname,"welcome",self.lastname,"to the class of",self.graduationyear)
# x=B("pavi", "hari",2019)
# x.hello()
#multiple inhiretans
# class Mother:
#   mothername=""
#   def mother(self):
#         print(self.mothername)
# class Father:
#  fathername=""
#  def father(self):
#         print(self.fathername)
# class son(Mother,Father):
#   def parents(self):
#         print("Father :",self.fathername)
#         print("Mather:",self.mothername)
# s1=son()
# s1.fathername='ram'
# s1.mothername='kavitha'
# s1.parents()

#multilevel
# class Mother:
#   mothername=""
#   def mother(self):
#         print(self.mothername)
# class Father(Mother):
#  fathername=""
#  def father(self):
#         print(self.fathername)
# class son(Father):
#     sonnmae=""
#     def son(self):
#         print(self. sonname)
#     def parents(self):
#         print("Father :",self.fathername)
#         print("Mather:",self.mothername)
#         print("son:",self.sonnmae)
# s1=son()
# s1.fathername='ram'
# s1.mothername='kavitha'
# s1.sonnmae='nani'
# # s1.parents()
# #hierarchical method
# class Parent:
#     def func1(self):
#         print("the function is parent class.")
# class child1(Parent):
#     def func2(self):
#         print("the function is child1.")
# class child2(Parent):
#     def func3(self):
# #         print("this function is child3 class.")
# object1=child1()
# object2=child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()
#
# #override differnt classes same method same  parametes is called overrriding
#  class A(object):
#    def add(self,a,b):
#      print ("i am in a class")
#  class B(A):
#    def add(self,a,b):
#      print (a-b)
#     j.B(A)
# j.add(10,20)
# j.add(10,30)

# #example
# a=10
# a=10
# print(a)
# class Parent:
#    def mymethod(self):
#        print('Calling parent method')
# class Child(Parent):
#     def mymethod(self):
#         print('Calling child method')
# c=Child()
# c.mymethod()
# def printme(str):  # functions
#     "this prints a passed string into this function"
#     print(str)
#     return;
# # printme(str="my string")
# def printinfo(name,age):
#     "this prints a passed info into this function"
#     print("Name:",name)
#     print("Age",age)
#     return;
# print(age=50,name="miki")
class A:
   def sum(self):
       print("calling from A-sum of 2 number is 15")
class B:
        def sum(self):
             print("calling from B-sum of 2 number is 14")
object1=A()
object1.sum()
object2=B()
object2.sum()
