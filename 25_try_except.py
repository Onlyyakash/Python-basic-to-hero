# a = input("enter a number: ")
# print(f"multiplication table of {a} is: ")
# try:
#    for i in range(1, 11):
#      print(f"{int(a)} * {i} = {int(a) * i}")
# except :
#       print("invalid")
# print("done")
# print("yahoo")


def func1():
  try:
      l = [1, 5, 6, 7]
      i = int(input("enter a number: "))
      print(l[i])
      return 1
  except :
      print("Index out of range")
      return 0
  finally:
      print("I am always executed")
x = func1()
print(x)

try:
    num = (int(input("enter a number: ")))
except ValueError:
    print("number entered is not a integer")


#try and except block to handle division by zero
try:
    result = 10 / num
except ZeroDivisionError:
    print("division by zero is not allowed")
else:
    print(f"The result of 10 divided by {num} is: {result}")
finally:
    print("Execution completed, whether an exception occurred or not.")

# Example of try-except with file handling
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'example.txt' was not found.")
except IOError:
    print("An error occurred while reading the file.")

# Example of try-except with a custom exception
class CustomError(Exception):
    """Custom exception class."""
    pass    
try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print(f"CustomError occurred: {e}")
# Example of try-except with multiple exceptions

try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"The result of 100 divided by {value} is: {result}")

# Example of try-except with a finally block
try:
    file = open("example.txt", "w")
    file.write("Hello, World!")
except IOError:
    print("An error occurred while writing to the file.")
finally:
    file.close()
    print("File closed.")

# Example of try-except with a context manager
try:
    with open("example.txt", "w") as file:
        file.write("Hello, World!")
except IOError:
    print("An error occurred while writing to the file.")

# Example of try-except with a context manager for reading a file
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'example.txt' was not found.")
except IOError:
    print("An error occurred while reading the file.")
    


# Example of try-except with a custom exception
class CustomError(Exception):
    """Custom exception class."""
    pass
try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print(f"CustomError occurred: {e}")




