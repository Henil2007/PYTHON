# a = int(input("Enter number : "))
# b = int(input("Enter number : "))

# c = a >= b
# d = a < b
# print(c)
# print(d)


# name = input("Enter name : ")
# dol = 0

# for i in name:
#     if(i == '$'):
#         dol += 1
# print(dol)


# num = int(input("Enter a number : "))
# if(num % 10 == 0):
#     print("Even number.")
# else:
#     print("Odd number.")


# a = int(input("Enter a number : "))
# b = int(input("Enter a number : "))
# c = int(input("Enter a number : "))

# if(a>b):
#     if(a>c):
#         print(a)
#     else:
#         print(c)
# else:
#     if(b>c):
#         print(b)
#     else:
#         print(c)

# num = int(input("Enter number : "))
# sum = 0
# i = 1
# while i <= num:
#     sum = sum + i
#     i += 1
# print(sum)

num = int(input("ENter number : "))
fac = 1
for i in range(num,0,-1):
    fac *= i
print(fac)