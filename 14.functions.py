# def avg(a,b,c):
#      l= (a+b+c)/3
#      print("average is",l)
# avg(7,9,3)

# #average function
# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("average is:",sum/len(numbers))
# average(2,4,6,8)

# #square function
# def square(n):
#     '''helper function to square a number'''
#     print(n**3)
# square(5)
# print(square.__doc__)

# #factorial function
# def factorial (n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def avg(a,b,c):
#      l= (a+b+c)/3
#     #  print("average is",l)
#      return l
# o1 = avg(5,8,25)
# o2 = avg(56,86,44)
# print(o1)
# print(o2)

#lambda function
# def double(x):
#     """Returns the double of the input value."""
#     return x * 2
# print(double(5))  """ Output: 10 """


double = lambda x: x*2
double = lambda x: x*x
'''As good as writing
def aquare(x):
    return x*x
    '''
cube = lambda x: x**3
avg = lambda x, y: (x + y) / 2
print(double(5))  # Output: 10
print(cube(5))    # Output: 125
print(avg(5,3))  # Output: 4.0

#fibonacci function(recursive)
def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(int(input("Enter a number: "))))