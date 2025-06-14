# A list is a collection which is ordered and changeable. Allows duplicate members.
# A list is written with square brackets.
# It is used to store multiple items in a single variable.
# A list is mutable, meaning its elements can be changed after creation.
# A list can contain any data type, including other lists, tuples, or dictionaries.
# A list can be used to store a collection of items that can be modified, such as adding or removing elements.
# list methods
l=[1,45,34,3,7,8,10,5,1,1,9]
print(l)

l.append(7) #this will change the original list by adding 7 at the end of the list
print(l)

l.sort() #this will sort the list in ascending order
print(l)

l.sort(reverse=True) #this will sort the list in descending order
print(l)

l.reverse() #this will reverse the list
print(l)

print(l.index(5)) #this will return the index of the first occurrence of 5 in the list

print(l.index(1, 2)) #this will return the index of the first occurrence of 1 in the list starting from index 2

print(l.count(1)) #this will return the count of occurrences of 1 in the list



m=l
m[2]=0 #this will change the original list by changing the value at index 2 to 0
print(l)


m=l.copy
m[2]=0
print(l) # this will not change the original list as m is a copy of l, not a reference to it
# m=l.copy() #this will create a copy of the list l

          
l.insert(1,222) #this will insert 222 at index 1 in the list
print(l)

m=[100,200,300,400,500] # this is a new list
# extending the list with another list
l.extend(m)
print(l)

# concatinating two lists
m=[100,200,300,400,500]
k=l+m
print(k)


# removing elements from list
l.remove(1)
print(l)


l.pop(2)
print(l)
# l.pop() #this will remove the last element from the list

l.clear() # this will remove all elements from the list
print(l)
