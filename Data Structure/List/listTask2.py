color = ["red","green","blue","orange","white","red"]

name = input("Enter color name : ")

if(name in color):
    color.remove(name)
    print(color)
else:
    print("color not present")