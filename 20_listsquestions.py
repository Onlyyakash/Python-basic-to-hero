#lists questions
# 1. Create a list of your favorite fruits and print it.
favorite_fruits = ["apple", "banana", "cherry"]
print(favorite_fruits)

# 2. Add a new fruit to the list and print the updated list.
favorite_fruits.append("orange")
print(favorite_fruits)

# 3. Remove a fruit from the list and print the updated list.
favorite_fruits.remove("banana")
print(favorite_fruits)

# 4. Print the number of fruits in the list.
print(len(favorite_fruits))

# 5. Check if a specific fruit is in the list.
print("apple" in favorite_fruits)

# 6. Sort the list of fruits in alphabetical order and print it.
favorite_fruits.sort()
print(favorite_fruits)

# 7. Reverse the order of the list and print it.
favorite_fruits.reverse()
print(favorite_fruits)

# 8. Create a new list that contains the lengths of each fruit name in the original list.
fruit_lengths = [len(fruit) for fruit in favorite_fruits]
print(fruit_lengths)

# 9. Create a list of numbers and find the maximum and minimum values in the list.
numbers = [10, 20, 5, 30, 15]
print(max(numbers))
print(min(numbers))

# 10. Create a list of numbers and calculate the sum and average of the numbers in the list.
numbers = [10, 20, 5, 30, 15]
print(sum(numbers))
print(sum(numbers) / len(numbers))

# 11. create a list containing the squares of the numbers in the original list.
squares = [num ** 2 for num in numbers]
print(squares)

# 12. Create a list of even numbers from 1 to 20.
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)

# 13. Create a list of odd numbers from 1 to 20.
odd_numbers = [num for num in range(1, 21) if num % 2 != 0]
print(odd_numbers)

# 14. create a list containing the table of 5.
table_of_5 = [5 * i for i in range(1, 11)]
print(table_of_5)

# 15. Create a list of the first 10 square numbers.
square_numbers = [i ** 2 for i in range(1, 11)]
print(square_numbers)

# 16. Create a list of the first 10 Fibonacci numbers.
def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

print(fibonacci(10))

# 17. Create a list of prime numbers between 1 and 50.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in range(1, 51) if is_prime(num)]
print(prime_numbers)

# 18. Create a list of the first 10 multiples of 3.
multiples_of_3 = [3 * i for i in range(1, 11)]
print(multiples_of_3)

# 19. create a list to check the number is palindrome or not.
def is_palindrome(num):
    return str(num) == str(num)[::-1]

palindrome_numbers = [num for num in range(1, 101) if is_palindrome(num)]
print(palindrome_numbers)

# 20. Create a list of tuples where each tuple contains a number and its square.
number_square_tuples = [(num, num ** 2) for num in range(1, 11)]
print(number_square_tuples)

# 21. Create a list of dictionaries where each dictionary contains a fruit and its color.
fruits_with_colors = [
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "cherry", "color": "red"},
    {"fruit": "orange", "color": "orange"}
]
print(fruits_with_colors)

# 22. create a list to check if a number is even or odd.
def is_even(num):
    return num % 2 == 0
def is_odd(num):
    return num % 2 != 0
even_odd_list = [{"number": num, "is_even": is_even(num), "is_odd": is_odd(num)} for num in range(1, 21)]
print(even_odd_list)

# 23. find max
A = [11, 23, 35, 47, 38, 25]
'''
print(max([i for i in A if i % 2 == 0]))  # Max even number
print(max([i for i in A if i % 2 != 0]))  # Max odd number
'''
print(max([i for i in A if i != max(A)]))  # Max excluding the max value
# 24. find min
'''
print(min([i for i in A if i % 2 == 0]))  # Min even number
print(min([i for i in A if i % 2 != 0]))  # Min odd number
'''
print(min([i for i in A if i != min(A)]))  # Min excluding the min value

# 25. Count even and odd numbers in a list
a = [23, 11, 44, 55, 30]
even = odd = 0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Even numbers: {even}, Odd numbers: {odd}")


# 26. Create a list of numbers and check if it contains any duplicates.
numbers_with_duplicates = [1, 2, 3, 4, 5, 1, 2]
has_duplicates = len(numbers_with_duplicates) != len(set(numbers_with_duplicates))
print("Contains duplicates:" if has_duplicates else "No duplicates found.")

# 26. Create a list of numbers and check if it is palindrom or not.
def is_palindrome_list(lst):
    return lst == lst[::-1]
numbers_to_check = [1, 2, 3, 2, 1]
print("Is palindrome:" if is_palindrome_list(numbers_to_check) else "Not a palindrome.")

# 27. Create a list of strings and find the longest string in the list.
def find_longest_string(strings):
    return max(strings, key=len)
strings_list = ["apple", "banana", "cherry", "watermelon"]
longest_string = find_longest_string(strings_list)
print("Longest string:", longest_string)
