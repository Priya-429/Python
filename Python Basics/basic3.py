age = 20
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
# WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN
num = int(input("enter number: "))
if(num % 2 == 0):
    print("even")
else:
    print("odd")
# WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER.
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
if(a >= b and a>=c):
    print("first number is largest",a)
elif(b >= c):
    print("second number is largest",b)
else:
    print("third is largest",c)
# WAP TO FIND THE GREATEST OF 2 NUMBERS ENTERED BY THE USER
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))
if(a >= b and a >= c and a >= d):
    print("the largest number is:",a)
elif(b >= c and c >= d):
    print("the largest number is:",b)
elif(c>=d):
    print("the largest value is:",c)
else:
    print("the largest value is:",d)
# wap to check if a number is a multiple of 7 or not
x = int(input("enter number: "))
if(x % 7 == 0):
    print("multiple of 5")
else:
    print("not a multiple")
    



