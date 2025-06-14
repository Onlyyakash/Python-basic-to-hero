# a = int(input("enter a number between 5 and 9: "))
# if(a < 5 or a > 9):
#     raise ValueError("Number is not in range")
a = input("Enter the value bw 5 and 9=")

if (a == "quit"):
    print("no error")
elif (int(a)<5 or int(a)>9):
    raise ValueError("Value should between 5 and 9")




