a = (input("Enter a number: "))
print(a)
print(type(a))  # <class 'str'>, since input() returns a string

b = (input("Enter your name: "))
print(b)

c = int(input("Enter your age: "))
print(c)
print(type(c))  # <class 'int'>, since we typecasted the input to int(if you write anything other than a number, it will throw an error)




# a = input("Enter first number: ")
# b = input("Enter second number: ")
# print("Sum:", a + b)  # This will concatenate the strings

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Sum:", a + b)  # This will add the two integers correctly



a = input("Enter first number: ")
print(a + 3)  # This will throw an error because a is a string and 3 is an integer, you cannot add a string and an integer directly

a = input("Enter first number: ")
a = int(a)  # Typecasting the input to integer
# Now you can add 3 to it
print(a + 3)  # This will work correctly, adding 3 to the integer value of a





