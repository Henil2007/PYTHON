no = 153
sum = 0
rem = 0
while(no > 0):
    rem = no % 10
    sum = sum + rem**3
    no = no // 10
r = 153
if(r == sum):
    print("number is Armstrong")