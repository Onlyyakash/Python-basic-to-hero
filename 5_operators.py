a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

# Arithmetic operators
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division (float result)
print("a // b =", a // b)  # Floor division (integer result)
print("a % b =", a % b)  # Modulus (remainder)
print("a ** b =", a ** b)  # Exponentiation (a raised to the power of b)

# Comparison operators
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)  # Greater than
print("a < b:", a < b)  # Less than
print("a >= b:", a >= b)  # Greater than or equal to

# Logical operators
c = True
d = False
print("c and d =", c and d)  # Logical AND
print("c and d =", c and c)  # Logical AND with both true
print("d and c =", d and c)  # Logical AND with one false
print("d and d =", d and d)  # Logical AND with both false


print("c or d =", c or d)  # Logical OR
print("c or d =", c or c)  # Logical OR with both true
print("d or c =", d or c)  # Logical OR with one false
print("d or d =", d or d)  # Logical OR with both false


print("not c =", not c)  # Logical NOT
print("not d =", not d)  # Logical NOT

# Bitwise operators

print("a & b =", a & b)  # Bitwise AND
print("a | b =", a | b)  # Bitwise OR
print("a ^ b =", a ^ b)  # Bitwise XOR
print("~a =", ~a)  # Bitwise NOT
print("a << 1 =", a << 1)  # Bitwise left shift
print("a >> 1 =", a >> 1)  # Bitwise right shift

# Assignment operators

a += b  # Equivalent to a = a + b
print("a after += b:", a)  # Output will be the new value of a after addition
a -= b  # Equivalent to a = a - b
print("a after -= b:", a)  # Output will be the new value of a after subtraction
a *= b  # Equivalent to a = a * b
print("a after *= b:", a)  # Output will be the new value of a after multiplication
