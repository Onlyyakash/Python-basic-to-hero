#tuple questions
# 1. Create a tuple with the names of five countries.
names = ("ramesh", "surendra", "gauti", "mohit", "chandu")

# 2. Access and print the second name in the tuple.
print(names[1])

# 3. Check if "shaktiman" is in the tuple and print the result.
print("shaktiman" in names)

# 4. Create a new tuple with the names of three more names.
more_names = ("bandiya", "gerango", "digamber", "mohit")

# 5. Concatenate the two tuples and print the result.
all_names = names + more_names
print(all_names)
'''
print(names.__add__(more_names))'''

# 6. Find and print the index of "gerango" in the concatenated tuple.
print(all_names.index("gerango"))

# 7. Count and print the number of times "mohit" appears in the concatenated tuple.
print(all_names.count("mohit"))

# 8. Create a tuple with the numbers 1 to 5.
numbers = (1, 2, 3, 4, 5)

# 9. Print the first and last elements of the numbers tuple.
print(numbers[0])
print(numbers[-1])

# 10. Create a nested tuple with the States and their capitals.
nested_tuple = (("Chhattisgarh", "Raipur"), ("Madhya Pradesh", "Bhopal"), ("Maharashtra", "Mumbai"))
for state, capital in nested_tuple:
    print(f"state: {state}, capital: {capital}")

# 11. Access and print the capital of "Madhya Pradesh" from the nested tuple.
print(nested_tuple[1][1])  # Accessing the capital of Madhya Pradesh

# 12. Create a tuple with mixed data types (string, integer, float).
mixed_tuple = ("Python", 3, 3.14, True)

# 13. Print the length of the mixed tuple.
print(len(mixed_tuple))

# 14. Create a tuple with the first five prime numbers.
prime_numbers = (2, 3, 5, 7, 11)

# 15. Print the prime numbers in reverse order.
print(prime_numbers[::-1])

# 16. Create a tuple with the first ten square numbers.
square_numbers = tuple(i ** 2 for i in range(1, 11))

