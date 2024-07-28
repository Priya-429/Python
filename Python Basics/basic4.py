marks = [94.4,87.5,95.2,66.4,45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))
student = ["karan",95.4,17,"delhi"]
print(student[0])
student[0] = "Arjun"
print(student[0])
marks = [87,94,98,74,76]
print(marks[1:4])
print(marks[ :4])
print(marks[1: ])
print(marks[-3:-1])
list = [2,3,1]
list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list = ['a','b','g','c']
list.sort()
print(list)
list.reverse()
print(list)
list = [2,1,3]
list.insert(1,5)
print(list)
list.remove(1)
print(list)
list.pop(2)
print(list)
tup = (2,1,3,1)
print(tup[0])
print(tup[1])
tup = ()
print(tup)
print(type(tup))
tup = (1,2,3,4)
print(tup.index(2))
print(tup.count(1))
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
# wap to check if a list contains a palindrome of elements
list1 = [1,2,1]
list2 = [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")
# wap to enter the number of students with the "A" grade in the following tuple
tup = ("A","B","C","A","D","B")
print(tup.count("A"))
# STORE THE AVOVE VALUES IN A LIST & SORT THEM FROM "A"TO"D
list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)
dict={
    "name" : "shradha",
    "cgpa" : 9.6,
    "marks" : [98,97,95],

}
print(dict)
info = {
    "name" : "apnacollege",
    "subjects" : ["python","c","java"],
    "topics" : ("dict","set"),
    "age" : 35,
    "is_adult" : True ,
    12.99 : 94.4

}
print(type(info))
print(info)
print(info["name"])
null_dict ={}
null_dict["name"] = "apnacollege"
print(null_dict)
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "che" : 98,
        "math" : 95,
    }
}
print(student["subjects"]["phy"])