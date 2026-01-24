# name = input("Enter name : ")
array = []

while(True):
    name = input("Enter name : ")
    # array = name
    if(name == "exit"):
        break
    else:
        array.append(name)       
print(array)