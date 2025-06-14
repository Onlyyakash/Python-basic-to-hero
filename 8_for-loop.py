#simple for loop example
#this loop will print numbers from 1 to 5
'''for i in range(1,6):
    print(i)'''

for i in range(12):
    if(i==10):
        break
    print("5 x",i+1,"=",5*(i+1))
print("loop se bahar")

for i in range(12):
    if(i==10):
        print("loop se bahar")
        continue
    print("5 x",i,"=",5*(i))

#for loop 
'''a = int(input("Enter a number: "))
for i in range(1, 11):
    print(a, "x", i, "=", a * i)'''

#for loop with if-else
user_input = input("Enter numbers: ")
numbers = [int(i) for i in user_input.split(",")]
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

#for loop patterns

a = int(input("enter a number: "))
for i in range(1, a+1):
    for j in range(i,a+1):
        print("*", end=" ")
    print()

import time
a = int(input("enter a number: "))
for i in range(1, a+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
    time.sleep(0.5)


a = int(input("Enter a number: "))
for i in range(1, a+1):
    print(" " * (a - i), end="")   # spaces
    print("* " * i)               # stars


# a = int(input("Enter a number: "))
for i in range(a, 0, -1):
    print(" " * (a - i), end="")   # spaces
    print("* " * i)               # stars


a = int(input("Enter size of square: "))
for i in range(1, a+1):
    for j in range(1, a+1):
        if i == 1 or i == a or j == 1 or j == a:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


