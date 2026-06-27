# decorators

# def greet():
#     print('hello')

# def my_decorator(func):
#     def wrapper():
#         print("before function execution")
#         func()
#         print(  "AFTER EXECUTION ")
#     return wrapper
# greet=my_decorator(greet)
# greet()
  
# 2.
# def greet(func):
#     def wrapper(name):
#         print("start")
#         result = func(name)   # call original function
#         print(result)         # print inside decorator
#         print("end")
#     return wrapper


# @greet
# def greeting(name):
#     return f"hello world {name}"


# greeting("amit")


a=input("enter somethin")
count=0
for ch in a:
    if ch in "aeiou":
        count+=1
print(count)