str1 = "this is a string."
str2 = 'apnacollege'
str3 = """this is a string"""
str4 = "this is a string.\n we are creating it in python"
print(str4)
str1 = "apna"
str2 = "college"
print(str1+str2)
str1 ="apna"
print(len(str1))
str2 = "college"
print(len(str2))
final_str = str1+str2
print(final_str)
print(len(str1))
print(len(final_str))
str1 = "priya"
print(len(str1))
str = "apna college"
print(str[3])
str = "apna college"
print(str[1:4])
print(str[5:len(str)])
str = "i am studying python from apnacollege"
print(str.capitalize())
print(str)
print(str.endswith("ege"))
print(str.replace("o","a"))
print(str.find("o"))
print(str.count("from"))
# WAP to input users first name & print its length
name = input("please enter your name: ")
print("length of your name is",len(name))
# WAP to find the occurrence of '$' in a string
str = "hi, $ i am the $ symbol $99.99"
print(str.count("$"))
# if-elif-else
age = 21
if (age >= 18):
    print("can vote & apply for licence")
light = "green"
if (light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")
print("end of the code")
age = 14
if(age >= 18):
    print("can vote")
else:
    print("cannot vote")
marks = 74
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif (marks >= 70 and marks < 80):
    grade = "c"
else:
    grade = "D"
print("grade of the student ->",grade)



