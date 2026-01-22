# write a program to check weather the entered string is palindrome or not.

name = input("Enter name : ")
rev = ""

i = len(name) - 1

while i >= 0:
    rev = rev + name[i]
    i = i - 1

if(name == rev):
    print("The string is Palindrome.")
else:
    print("THe string is not Palindrome.")
