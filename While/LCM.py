a = int(input("Enter number : "))
b = int(input("Enter number : "))
max = 0
LCM = 0
if(a>b):
    max = a
else:
    max = b

while True:
    if(a % max == 0 and b % max == 0):
        max +=1
LCM = max
print(lcm)