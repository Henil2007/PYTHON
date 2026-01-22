data = "javascript"

data = data.replace("a","#",4)
print(data)

data1 = "Java script is java"
replacedata = ""

for i in range(len(data1)):
    if i >= 2 and data1[i] == "a":
        replacedata += "A"
    else:
        replacedata += data1[i]

print(replacedata)