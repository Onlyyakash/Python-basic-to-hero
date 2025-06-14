a = int(input("Enter your lucky draw 1-5: "))
match a:
    case 1:
        print("you cant get anything")
    case 2:
        print("you will get a car")
    case 3:
        print("you'll get a mango bite")
    case 4:
        print("you'll get a thenga")
    case 5:
        print("you'll get a chocolate")
    case _:
        print("you'll get nothing")
        
