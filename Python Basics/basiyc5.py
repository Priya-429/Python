student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }

}
print(student["subjects"])
print(student.keys())
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))
print(student.values())
print(student.items())
pairs = list(student.items())
print(pairs[0])
student.update({})
print(student.get("name"))
student.update({'city':'delhi'})
print(student)