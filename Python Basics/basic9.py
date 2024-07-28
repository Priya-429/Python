# def int_num ():
#     n = int(input("enter the number you want to print ="))
#     if (n%2 == 0):
#         print("even")
#     else:
#         print("odd")
# a = 10
# b = 20
# sum = a+b
# print(sum)
# diff = a-b
# print(diff)
# # oops in python
# class Student:
#     name = "karan kumar"
# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)
# class Student:
#     name = "karan"
#     def _init_(self):
#         print("adding new student in database")
# print(s1)
# list_a = [1,2,3]
# list_b = [4,5,6]
# output = list_a + list_b
# print(output)
# variable_a = 10
# if variable_a < 10:
#     print(variable_a)
# else:
#     print("invaild syntex")
# a = int(input("enter the value you want to print =  "))
# b = int(input("enter the value you want to print =  "))
# sum = a+b
# print(sum)
# input_varaible = input("please enter your name\n")
# print("hello",input_varaible)
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# for i in range (101):
#     print(i)
# basic_list = ["python","java","cpp"]
# for i in basic_list:
#     print(i)
# my_dict = {
#     "raunak" : "joshi",
#     "john"   : "rex",
#     "priya"  : "deb",
#     "clark"  : "kent"
# }
# for i,j in my_dict.items():
#     print(i,j)
# def basic_function ():
#     return "hi world"
# print(basic_function())
# print(basic_function())
# print(basic_function())
# print(basic_function())
# print(basic_function())
# print(basic_function())
# print(basic_function())
# print(basic_function())
# print(basic_function())
# def dollar_to_inr(dollars):
#     inr = dollars * 74.93
#     return inr
# print(dollar_to_inr(2))
# print(dollar_to_inr(float(input("enter the number of dollars\n"))))
# class Name :
#     def __init__ (self,name):
#         print("hello" +name)
# n = Name(input("please enter your name\n"))
# printa("hello")
# try:
#     printa("hello world")
# except NameError:
    # print("something is wrong")
# while True:
#     try:
#         number_a = 10
#         number_b = int(input("enter number b \n"))
#         division = number_a / number_b
#         print(division)
#         break
#     except Exception:
#         print("something is wrong with your code")
#     finally:
#         print("code execution has finished")
class Student:
    name = "karan"
s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)
class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)
class Student:
    name = "karan"
    def __init__(self,name,marks):
        self.name  = name
        self.marks = marks
        print("adding new student in database..")
s1 = Student("karan",97)
print(s1.name)
s2 = Student("arjun",88)
print(s2.name,s2.marks)



