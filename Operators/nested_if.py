age = int(input("Enter your age: "))
if age >= 18 :
    print("Eligible for voting")
    if age > 22 :
        print("Eligible for marrage.")
    else :
        print("Not eligible for marrage")
else :
    print("Not eligible for voting")
    if(age > 5) :
        print("Eligible for schooling")
    else :
        print("Stay at home")