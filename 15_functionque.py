#addition of two number using add function
def add (x,y):
    ans = x + y
    return ans
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = add(a,b)
print(f"The sum of {a}+{b} = {c}")


# Function to calculate the area of a rectangle
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print(f"The area of the rectangle is {area}")

# Function to check if a number is prime
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Function to find the maximum of three numbers
def find_maximum(a, b, c):
    """Find the maximum of three numbers."""
    return max(a, b, c)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
maximum = find_maximum(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is {maximum}")

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F.")


# Function to reverse a string
def reverse_string(s):
    """Reverse a given string."""
    return s[::-1]      
string_input = input("Enter a string to reverse: ")
reversed_string = reverse_string(string_input)
print(f"The reversed string is: {reversed_string}")


# Function to calculate the factorial of a number
def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number to calculate its factorial: "))
fact = factorial(number)
print(f"The factorial of {number} is {fact}.")


# Function to check if a string is a palindrome
def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.lower().replace(" ", "")  # Normalize the string
    return s == s[::-1]
string_input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string_input):
    print(f"{string_input} is a palindrome.")
else:
    print(f"{string_input} is not a palindrome.")

#function to check the number is palindrome or not
def is_number_palindrome(n):
    """Check if a number is a palindrome."""
    str_n = str(n)
    return str_n == str_n[::-1]
number = int(input("Enter a number to check if it's a palindrome: "))
if is_number_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

#alternative way to check if a number is palindrome
def palindrome(n):
    if (str(n) == str(n)[::-1]):
        return True
    a = [11,45,123,141,657,666,129,291]
    for i in a:
        if palindrome(i):
            print(f"{i} is a palindrome")
        else:
            print(f"{i} is not a palindrome")

# Function to calculate the sum of digits in a number
def sum_of_digits(n):
    """Calculate the sum of digits in a number."""
    return sum(int(digit) for digit in str(n))
number = int(input("Enter a number to calculate the sum of its digits: "))
digit_sum = sum_of_digits(number)
print(f"The sum of digits in {number} is {digit_sum}.")


# Function to calculate the sum and multiplication of a list of numbers
# This code defines a decorator to enhance the functionality of the add and mult functions
def imp(base):
    def temp(n):
        c= len(n)
        print("number of values = ", c)
        base(n)
    return temp
def add(l):
    sum = 0
    for i in range(len(l)):
        sum=sum+l[i]
    print("sum of all values = ", sum)

def mult(l):
    ans=1
    for i in range(len(l)):
        ans=ans*l[i]
    print("multiplication of all values = ", ans)

a = [5,4,8,10,3,2,1]
add(a)
mult(a)
add = imp(add)
mult = imp(mult)
print("\n after improvement: ")
print()
mult(a)
