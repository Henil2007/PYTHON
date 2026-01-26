color = ["red","green","blue","orange","orange","white","red"]

ul = []

for i in color:
    if i not in ul:
        ul.append(i)
print(ul)