#simple while loop
'''i = 1
while i < 6:
    print(i)
    i = i+1
    
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
    
a = int(input("enter a number: "))
i = 1
while i<=10:
    print(a,"x",i, "=", a*i)
    i = i+1'''


#while loop with if else
'''a = int(input("Enter a number: "))
count = 1

while count <= a:
    num = int(input(f"[{count}] Enter a number: "))
    
    if num % 2 == 0:
        print("Even number\n")
    else:
        print("Odd number\n")
    
    count += 1'''

#while loop patterns

a = int(input("Enter a number: "))
i = 1
while i<=a:
    j = 1
    while j<=i:
        print("*", end=" ")
        j = j+1
    print()
    i = i+1


a = int(input("enter a number: "))
i = 1
while i<= a:
    j = i
    while j<=5:
        print(j,end="")
        j+=1
    print()
    i+=1


a = int(input("Enter a number: "))
i = 5
while i>=1:
    j = i
    while j<=5:
        print(j,end="")
        j+=1
    print()
    i-=1


a = int(input("Enter a number: "))
i = 1
while i<= a:
    j = a-i+1
    while j>=1:
        print(j, end=" ")
        j -= 1
    print()
    i += 1


a = int(input("Enter a number: "))
i = 1
while i<=a:
    j = 1
    while j<= a:
        print("*",end=" ")
        j = j + 1
    print()
    a = a - 1


a = 1
i = int(input("Enter a number: "))
while i >= a:
    j = 1
    while j<= i:
        print("*", end=" ")
        j = j+1
    print()
    i=i-1


a = int(input("Enter a number: "))
i = 1
while i<=a:
    j = 1
    while j<=a - i:
        print(" ",end=" ")
        j=j+1
    k = 1
    while k<=2*i - 1:
        print("*",end =" ")
        k = k+1
    print()
    i = i + 1


a = int(input("Enter a number: "))
i = a
while i>=1:
    j = 1
    while j<=a-i:
        print(" ",end=" ")
        j=j+1
    k = 1
    while k<=2*i - 1:
        print("*",end =" ")
        k = k+1
    print()
    i = i - 1
 

import time
a = int(input("Enter a number: "))
i = 1
while i<=a:
    j = 1
    while j<=a - i:
        print(" ",end=" ")
        j=j+1
    k = 1
    while k<=2*i - 1:
        print("*",end =" ")
        k = k+1
    print()
    i = i + 1
    time.sleep(0.5)
i = a - 1
while i>=1:
    j = 1
    while j<=a-i:
        print(" ",end=" ")
        j=j+1
    k = 1
    while k<=2*i - 1:
        print("*",end =" ")
        k = k+1
    print()
    i = i - 1
    time.sleep(0.5)


import time
a = int(input("Enter a number: "))
i = 1
while i<=a:
    j = 1
    while j<=a - i:
        print(" ",end=" ")
        j=j+1
    k = 1
    while k<=2*i - 1:
        print("🌟",end =" ")
        k = k+1
    print()
    i = i + 1
    time.sleep(0.5)
i = a - 1
while i>=1:
    j = 1
    while j<=a-i:
        print(" ",end=" ")
        j=j+1
    k = 1
    while k<=2*i - 1:
        print("🌟",end =" ")
        k = k+1
    print()
    i = i - 1
    time.sleep(0.5)
    

#factorial with while loop
'''a=int(input("Enter a number: "))
i=1
fact=1
while i<=a:
    fact = fact*i
    i += 1
print("Factorial of",a,"i =", fact)'''


#prime number
a = int(input("Enter a number: "))
i = 1
count = 0
while i < a:
    if a % i == 0:
        count += 1
    i += 1
if count == 0:
     print( "is a prime number")
else:
     print( "is not a prime number")


