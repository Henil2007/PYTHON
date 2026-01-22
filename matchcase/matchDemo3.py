choice = input(f" Press y for continue and n for exit\n Enter choice : ")

match choice :
    case "y" | "Y" | "yes":
        print("Continue...")
    case "n" | "N" | "no" :
        print("Exit...")
    case _ :
        print("Enter valid choice")