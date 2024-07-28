# class Student:
#     name = "karan"
# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)
# class Car:
#     color = "blue"
# car1 = Car()
# print(car1.color)
class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
def welcomeAboard(name):
    print("Welcome",name)  # Your code here
