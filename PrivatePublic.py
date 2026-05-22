# access the private variable:
# class Account:
#   __name="anonymous"
    

#   def show(self):
#    print(self.__name)
# p1= Account()
# p1.show()

# 2
# class Person:
#     __name="anonymous"

#     def __hello(self):
#         print("hello person")
    
#     def welcome(self):
#         self.__hello()
# p1=Person()
# print(p1.welcome())


# class A:
#     language="java"
#     slave_name="kashi"
# amit=A()
# amit.language="PYTHON"....this thing overrides the class attribute because of the priority on instance attribute over the class attribute
# print(amit.language,amit.slave_name,sep="\n")

#print them inside the method
#  class Studnet:
#     def dun(self):
#      self.name="daddy"
#      self.gansu=12
#      print (self.name,self.gansu)
# st=Studnet()
# st.dun()


# create class then call that attribute with another 
# class Student:
#     def unit(self):
#         self.name="amit"
#         self.age=12
#     def unit1(self):
#         return(f"the name is {self.name} and the age is {self.age}")
# s1=Student()
# s1.unit()
# print(s1.unit1())

# Calculator for taking the user for cube, sqrt etc..
import math
# class Calculator:
#     def init(self,a):
#       a=int(input("enter a number for cube: "))
#       return a**3
#     def square(self,a):
#         a=int(input("enter a number for square: "))
#         return a**2
#     def square_root(self,a):
#        a=int(input("enter a number for square root: "))
#        return math.sqrt(a)

# s1=Calculator()
# print(s1.cube(12))
# print(s1.square(12))
# print(s1.square_root(12))
    
# by using the constructor:

# q3