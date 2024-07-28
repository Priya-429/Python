collection = { 1,2,3}
print(collection)
print(type(collection))
collection = { 1,2,2,"hello","world",4}
print(collection)
print(len(collection))
collection = set()
collection.add (1)
collection.add(2)
collection.add(3)
collection.add(4)
print(collection)
collection.remove(2)
print(collection)
collection.clear()
print(collection)
collection = {"hello","apnacollege","world"}
collection.pop()
print(collection)
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
# store following word meanings in a pythion dictionary
dict = {
    "table" : ["a piece of furniture ", "list of facts & figures"],
    "cat" : "a small animal"
}
print(dict)
# you are given a list of subjects for students .assume one classroom is required for 1 subject .how many classrooms are needed by all students.
subject = { 
    "python","java","c++","python","javascript","java",
    "python","java","c++","c"
}
print(subject)
print(len(subject))
# wap to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary & add one by one. use subject name as key & marks as value.
marks = {}
x = int(input("enter phy : "))
marks.update ({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update ({"chem" : x})

print(marks)

# figure out a way to store 9 & 9.0 as separate values in the set
values = {
    ("float" , 9.0),
    ("int" , 9)
}
print(values)
count = 1
while count <= 5:
    print("hello")
    count += 1
print(count)
i = 1
while i <= 5:
    print(i)
    i += 1
prin("loop ended")