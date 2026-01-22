# factorial of a number input by user

a = int(input("Enter number a : "))
factorial = 1

for i in range(1,a+1):
    factorial = i * factorial

print("factorial = ",factorial)