# try:
#     l = [1,5,6,7]
#     i = int(input("enter the index: "))
#     print(l[i])
# except:
#     print("some error occurred")
#  while using the finally keyword   
try:
    l = [1,2,3,4]
    i = int(input("enter the index"))
    print(l[i])
except:
    print("some error occurred")
finally:
    print("i am always executed")
# why we have to use finally keyword 
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("i am always executed")
    x = func1()
    print(x)