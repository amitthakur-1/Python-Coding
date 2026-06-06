# print("hello world")

# 2.table of n
# n=int(input("enter number : "))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")

# 3. 
# n=input("enter your name: ")
# print(f"your name is {n}")

# 4.
# a=int(input("a= "))
# b=int(input("b= "))
# c=int(input("c= "))
# if a==b==c:
#     print("All are equal")
# elif a>=b and a>=c:
#     print(f"{a} is greater")
# elif b>=a and b>=c:
#     print("{b} is greater")
# elif c>=a and c>=b:
#     print("{c} is greater")
# else:
#     print("enter wrong choice")

 # 5.
# a = int(input("a= "))
# b = int(input("b= "))

# a = a + b
# b = a - b  # b = (a+b) - b = a
# a = a - b  # a = (a+b) - a = b

# print(f"a= {a}, b= {b}")

# 6 factorial 
# n=int(input("enter a number: "))
# f=1
# for i in range(1,n+1):
#   f=f*i
#   n+=1
# print(f"the factorial of number is :{f}")

# n=int(input("enter a number: "))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z, end=" ")
#     x=y
#     y=z
#     z=x+y

# class Person:
#     def display(self):
#         print("i am a parent class")
# class Student(Person):
#      pass
# s=Student()
# s.display()

# def , fun(*args):
#     print(args)
# fun(12,2,3,34)

# def student(**kwargs):
#     for key,value in kwargs.items():
#         print(key,":",value)
# student(name="Amit")
# a=20
# b=10
# print(a/b)
# print(a//b)
# print(a%b)

# a={12,23,11}
# print((a))

# import pandas as pd
# import numpy as np
# # s=pd.Series([10,20,30,40])
# s=pd.DataFrame([12,2,4,2,1,31,3,4,2,4,3],
# columns=["Numbers"])
# print(s)

# n=5
# for i in range(1,n+1):
#  for j in range(1,i+1):
#     print(j,end=" ")
#  print()


# matrix=[[1,2,3,4],[12,13,14,15]]
# matrix_copy=matrix.copy()
# # matrix_copy.append(45)
# # matrix[0][0]=455

# print("original   " ,matrix)
# print("copy       ",matrix_copy)


# n=5
# for i in range(n,0,-1):
#     print("*"*i)

# n=5
# for i in range(1,n):
#     print(" "*(n-i)+"*" * (2*i-1))

# n=5
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# n=5
# fact=1
# for i in range (1,n+1):
#     fact=fact*i
# print(fact)

# class student:
#     def __init__(self,name):
#         self.fullname=name
#         print("add new name")
        
# s1=student("amnqq")
# print(s1.fullname)

def decorator(func):
    def wrapper():
        print("hello")
        func()
        print("tq")

    return wrapper
@decorator
def greet():
    print("this is the name fun")
greet()


