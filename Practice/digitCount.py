name = "henil@  2007"
digit =0
alpha = 0
special = 0
space = 0
for i in name:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alpha += 1
    elif i.isspace():
        space+= 1
    else:
        special += 1
print(digit)
print(alpha)
print(space)
print(special)