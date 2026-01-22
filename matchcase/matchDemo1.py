choice = int(input(f" Enter 1 for addition\n Enter 2 for sub\n Enter 3 for multiplication\n Enter the choice : "))

match choice :
    
    case 1 : 
        print("Addition block")
    case 2 : 
        print("Substraction block")
    case 3 : 
        print("Multiplication block")
    case _ :
        print("Enter valid choice...");