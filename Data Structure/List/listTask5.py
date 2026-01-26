color = ["red","green","blue","orange","orange","green","white","red"]

ul = []
rl = []
rep = 0

for i in color:
    if i not in ul:
        ul.append(i)
    else:
        rl.append(i)
        rep += 1
print(ul)
print(rl)
print(rep)