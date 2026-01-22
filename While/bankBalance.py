a = int(input("Enter bank Balance : "))

while a > 0:
    if(a < 10000):
        print("Invalid Bank Balance")
        break
    elif(a >= 10000):
        print("Account Open")