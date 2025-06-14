#global variables example
def sum(a,b):
    """Calculate the sum of two numbers."""
    print("hey im a function")
    c = a + b
    global z  # Use the global variable z
    z = 0 #this will refer to the global variable z
    return c
z = 47
print(sum(5, 10))  # Output: 15
print(z)


#docstring example
def multiply(a, b):
    """Multiply two numbers."""
    return a * b
print(multiply(5, 10))  # Output: 50
print(multiply.__doc__)  # Output: Multiply two numbers.
# another example

def square(n):
    '''helper function to square a number'''
    print(n**3)
square(5)
print(square.__doc__)