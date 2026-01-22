a = int(input("Enter number a : "))
b = int(input("Enter number b : "))

choice = int(input(f"1.For Addition\n2.FOr Substraction\n3.For multiplication\n4.For Division\nEnter the choice : "))

match choice:

    case 1 : 
        c = a + b
        print("Addition is : ",c)
    
    case 2 :
        c = a - b
        print("Substraction is : ",c)
    
    case 3 : 
        c = a * b
        print("Multiplication is : ",c)

    case 4 :
        if(b == 0) :
            print("Undefined")
        else :
            c = a / b
            print("Division is : ",c)
    
    case _ :
        print("Enter a valid choice")