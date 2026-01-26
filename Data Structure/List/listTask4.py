color = ["red","green","blue","orange","orange","white","red"]

ul = []
rl = []

for i in color:
    if i not in ul:
        ul.append(i)
    else:
        rl.append(i)
print(ul)
print(rl)