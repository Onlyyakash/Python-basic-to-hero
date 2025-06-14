# sets

s = {1, 2, 3, 2, 4, 2, 5}
print(s)

info = {1, 'one', False, 1.2, "yoyoyo"}
print(info)

gogo = set()
print(type(gogo))

for value in info:
    print(value)
    # if value == 1:
    #     print("Found it")
    #     break

print("Length of info set:", len(info))

# Checking membership in a set
print("Is 1 in info set?", 1 in info)

# Checking if a set is empty
print("Is info set empty?", len(info) == 0)

# Set operations
print("Union of s and info:", s.union(info))

print("Intersection of s and info:", s.intersection(info))

print("Difference of s and info:", s.difference(info))

# Set comprehension
squared_set = {x ** 2 for x in range(1, 6)}
print("Squared set:", squared_set
      )
# Set methods
print("Is info set a subset of s?", info.issubset(s))
print("Is s a superset of info?", s.issuperset(info))

# Adding and removing elements from a set
print("Original info set:", info)

# Adding elements to a set
info.add("new_element")
print("Updated info set:", info)

# Removing elements from a set
info.remove(1)

print("After removing 1:", info)
# info.remove(100)  # This will raise a KeyError if 100 is not in the set

# Using discard to remove an element without raising an error
info.discard(100)  # This will not raise an error if 100 is not in the set
print("After discarding 100:", info)





# sets methods
cities1 = {'raigarh', 'raipur1', 'bilaspur2', 'kawardha'}
cities2 = {'new york', 'raipur', 'los angeles', 'bilaspur'}
# cities3 = cities1.union(cities2)
# cities3 = cities1.intersection(cities2)
# cities3 = cities1.difference(cities2)
# cities3 = cities1.symmetric_difference(cities2)
# print(cities1.issuperset(cities2))
# print(cities1.isdisjoint(cities2))
# print(cities2)
# cities3 = {"seol", "raipur", "kabul"}
# print(cities1.issuperset(cities3))
cities1.add("helsinki")
print(cities1)


emp1 = {111:55, 121: 65, 131: 75, 141: 85}
emp2 = {212:70, 222: 90, 232: 75 }
# emp1.update(emp2)
# emp1.clear()
# emp1.pop(121)
emp1.popitem()
del emp1[111]
print(emp1)