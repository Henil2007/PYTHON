#task 1
# check string is palidrome or not using sllicing : naman  

name = input("Enter name : ")

x = name[len(name)::-1]

if(name == x) :
    print("palindrom")
else:
    print("not Palindrom")