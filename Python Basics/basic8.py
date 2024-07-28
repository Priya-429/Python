
# i = 0 
# while i <= 5 :
#     print(i)
#     i += 1 
i = 0
while i <= 5:
    if (i == 3):
        break
    i += 1
    print(i)
print("end of the loop")


i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue
    print(i)
    i += 1
nums = [1,2,3,4,5]
for val in nums :
    print(val)
tup = (1,2,3,4,2,8,9) 
for num in tup:
    print(num)
else:
    print("end")
# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
num = [1,4,9,16,25,36,49,64,81,100]
for val in num:
    print(val)
# search for a number x in this tuple using loop:
num = [1,4,9,16,25,36,49,64,81,100]
x = 36 
idx = 0
for val in num :
    if (val == x):
        print("number found at idx",idx)
        break
    idx += 1
for i in range (10):
    print(i)
for i in range (2,10):
    print(i)
for i in range (2,10,2): #start#stop#step
    print(i)
# print numbers from 1 to 100. 
for i in range(1,101):
    print(i)
# print numbers from 100 to 1 .
for i in range(100,0,-1):
    print(i)
# print the multiplication table of a number n.
n = int(input("enter the number you want to print = "))
for i in range (1,11):
    print(i*n)
# print numbers from 1 to 100 by using while loop:
i = 1
while i <= 100:
    print(i)
    i += 1
# print numbers from 100 to 1.
i = 100
while i >= 1:
    print(i)
    i -= 1
# print the multiplication table of a number n.
n = int (input("enter the number you want to print = "))
i = 1
while i <= 10:
    print(n*i)
    i += 1

for i in range(5):
    pass
if i > 5:
    pass
print("some useful work")


# wap to find the sum of first n numbers
n = 5
sum = 0
for i in range (1,n+1):
    sum += i 
print("total sum =",sum)
# by using while loop
n = 7 
sum = 0 
i = 1 
while i <= n :
    sum  += i 
    i += 1
print("total sum = ",sum)
# wap to find the factorialnof first n numbers by using for loop
n = 4 
fact = 1
i = 1
while i <= n :
    fact *= i
    i += 1
    print("factorial =",fact)

n = 5 
fact = 1
for i in range (1,n+1):
    fact *= i
    print("factorial = ",fact)

def calc_sum (a,b):
    sum = a + b
    print(sum)
    return sum

calc_sum (2,10)
calc_sum (7,13)
def calc_avg (a,b,c):
    sum = a+ b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg  (1,2,3)
calc_avg (96,95,99)
print("apnacollege","priya",end = " ")
print("manabika")
# wap to print the length of a list.
cities = ["delhi","gurgaon","noida","pune","mumbai"]
heroes = ["thor","ironman","captain","america"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)


# wap to print the elements of a list in a single line .
def print_list(list):
    for item in list:
        print(item,end = " ")
# waf to find the factorial of n.
def cal_fact (n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
cal_fact(5)
cal_fact(6)
# waf to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val *83
    print(usd_val,"USD = ",inr_val,"INR")
converter(1)
def int_num ():
    n = int(input("enter the number you want to print ="))
    if (n%2 == 0):
        print("even")
    else:
        print("odd")

