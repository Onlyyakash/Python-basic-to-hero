#find biggest word in paragraph
s1 = "mango anuj go harry coconut he"
words = s1.split()
biggest_word = max(words,key=len)
print(f"The biggest word in the paragraph is: {biggest_word}")
# Output: The biggest word in the paragraph is: coconut

# find smallest word in paragraph
smallest_word = min(words,key=len)
print(f"The smallest word in the paragraph is: {smallest_word}")
# Output: The smallest word in the paragraph is: he

# find the number of vowels in a paragraph
vowels = "aeiou"
count = sum(1 for char in s1 if char in vowels)
print(f"The number of vowels in the paragraph is: {count}")
# Output: The number of vowels in the paragraph is: 10


#find the max size of a word in a paragraph
s2 = "mango anuj go harry coconut he"
s2 = s2.split(" ")
print(s2)
# max = len(s2[0])
'''for word in s2:
    if len(word) > max:
        max = len(word)
print(f"The max size of a word in the paragraph is: {max}")
# Output: The max size of a word in the paragraph is: 7'''

# Alternative way to find the max size of a word in a paragraph
'''
maxw = s2[0]
for i in s2:
    if max<len(i):
        max = len(i)
        maxw = i
    print("word: ", maxw, "size: ", max)
    '''
# Output: The max size of a word in the paragraph is: 7

# Alternative way to find the max size of a word in a paragraph

max_size = max(len(word) for word in s2)
print(f"The max size of a word in the paragraph is: {max_size}")
max_size = max(s2, key=len)
print(f"The max size of a word in the paragraph is: {max_size}")
max_size = max(s2, key=lambda x: len(x))
print(f"The max size of a word in the paragraph is: {max_size}")
# Output: The max size of a word in the paragraph is: coconut



#find the min size of a word in a paragraph

min_size = min(s2, key=lambda x: len(x))
print(f"The min size of a word in the paragraph is: {min_size}")

# Output: The min size of a word in the paragraph is: he

#positive statement to negative statement with string methods
# positive_statement = "I am happy"
# negative_statement = positive_statement.replace("happy", "not happy")
# print(f"Positive statement: {positive_statement}")
# print(f"Negative statement: {negative_statement}")

#alternative way to convert a positive statement to a negative statement

s = "they are good person"
s1 = s.split(" ")
s2 = []
'''
if "not" not in s1:
    s2 = s1[:2]+["not"]+s1[2:]
else:
    s2 = s1[:2]+s2[3:]
s3 = " ".join(s2)
print(s3)
'''

for i in s1:
    if i == "good":
        s2.append("not good")
    else:
        s2.append(i)
s3 = " ".join(s2)
print(f"Positive statement: {s}")
print(f"Negative statement: {s3}")