name = input("Enter name : ")
lowerName = ""

for i in name:
    if ord(i) <= 65 and ord(i) > 97:
        lowerName = lowerName + chr(ord(i) + 32)
    else:
        lowerName = lowerName + i

print(lowerName)