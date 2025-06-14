# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# A tuple is written with round brackets.
# It is used to store multiple items in a single variable.
# It is similar to a list, but the main difference is that tuples are immutable, meaning they cannot be changed after creation.
# A tuple is more memory efficient than a list.
# A tuple can contain any data type, including other tuples, lists, or dictionaries.
# A tuple can be used as a key in a dictionary, while a list cannot.
# A tuple can be unpacked into multiple variables, allowing for easy assignment of values.
# A tuple is mutable, meaning its elements cannot be changed, but the tuple itself can be reassigned to a new tuple.
# A tuple can be used to return multiple values from a function, making it useful for functions that need to return more than one value.
tup=(1,2,3,4,5,5)
print(type(tup))
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])

#tuple with one element
tup1 = (1,) # This is how you define a tuple with one element(the comma is always required)

countries = ("spain", "italy", "india", "england", "germany")
temp = list(countries)
temp.append("russia")
temp.pop(3)
temp[2] = ("finland")
countries = tuple(temp)
print(countries)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
# res = tuple1.count(2)
# res = tuple1.index(3)
# res = tuple1.index(3,4,8)
res = len(tuple1) 
print("count of 3 in tuple is:", res)

# tuple unpacking
a, b, c, d = (1, 2, 3, 4)
print("Unpacked values:", a, b, c, d)
'''
a = (1, 2, 3, 4)
(a1, a2, a3, a4) = a  # Tuple unpacking
print("Unpacked values:", a1, a2, a3, a4)

'''

# tuple with different data types
mixed_tuple = (1, "hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# nested tuple
nested_tuple = (1, (2, 3), (4, 5, (6, 7)))
print("Nested tuple:", nested_tuple)

# tuple comprehension
tuple_comprehension = tuple(x * 2 for x in range(5))
print("Tuple comprehension:", tuple_comprehension)

# tuple methods
print("Count of 2 in tuple1:", tuple1.count(2))  # Count occurrences of 2
print("Index of first occurrence of 3 in tuple1:", tuple1.index(3))  # Index of first occurrence of 3
print("Index of first occurrence of 3 after index 4 in tuple1:", tuple1.index(3, 4))  # Index of first occurrence of 3 after index 4

# tuple concatenation
tuple2 = (8, 9, 10)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# tuple slicing
sliced_tuple = concatenated_tuple[2:5]  # Slicing from index 2 to 4
print("Sliced tuple:", sliced_tuple)  # Output: (2, 3, 2)

# tuple sorting (tuples are immutable, so we convert to list for sorting)
sorted_tuple = tuple(sorted(concatenated_tuple))
print("Sorted tuple:", sorted_tuple)  # Output: (0, 1, 2, 3, 3, 3, 4, 5, 8, 9, 10)

# tuple iteration
for item in concatenated_tuple:
    print(item, end=' ')  # Output: 1 2 3 4 5 5 8 9 10

# tuple length
print("Length of concatenated tuple:", len(concatenated_tuple))  # Output: 9

# tuple membership
print("Is 3 in concatenated tuple?", 3 in concatenated_tuple)  # Output: True
       