# l=[1,3,4]
# print(l)
# print(type(l))



# marks=[3,5,6,"harry",True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])


# marks=[3,5,6,"harry",True]
# print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[5-3])
# print(marks[2])



marks=[3,5,6,"harry",True,7,8,9,10,11,12]
print(marks)
print(marks[1:8])
print(marks[1:8:2])
print(marks[1:8:3])



lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)


a = [11, 23, 35, 47, 38,67, 25]
print(max([i for i in a if i != max(a)]))
a = [11, 23, 35, 47, 38,67, 25]
print(max([i for i in a if i <= max(a)]))