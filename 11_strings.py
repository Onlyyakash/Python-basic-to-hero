'''name = "Akash"
# print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
'''

# apple = "Welcome to python world"
# for character in apple:
#     print(character)


# names="Akash0123456789"
# # print(names[0:2])
# # print(names[3:-2])
# # print(names[0:10])
# # print(len(names))
# print(names[0:10:1])#skip 0 character
# print(names[0:10:2])#skip 1 character


a = "Akash"
b = "deku!!!"
c = "zig"
d = "hey welcome to python"
l = "apple,banana,graphes,papaya"
text = "Hey what are you doing?"
print(a)
print(len(a))
print(a.lower())
print(a.upper())
print(b.rstrip("!"))
print(a.replace("Akash","AK"))
print(b.replace("deku!!!","medoriya"))
print(c.replace("zig","zag"))
print(l.split(","))
print(d.capitalize())
print(d.title())
print(text.swapcase())
print(text.find("are"))
print(text.replace("what","why"))


#fstring
letter = "my name is {} and im from {}"
name="akash"
place="raigarh"
print(letter.format(name,place))
# Output: my name is akash and im from raigarh
# print(letter.format(name,place).title())
# Output: My Name Is Akash And Im From Raigarh
print(f"my name is {name} and im from {place}")
# this is a f-string, which is a more modern way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}.
# f-strings are evaluated at runtime and can include any valid Python expression.
# f-strings are more readable and concise than the older string formatting methods, such as the format() method or the % operator.
# f-strings are also faster than the older methods, as they are evaluated at runtime and do not require any additional function calls.
price = 49.099999
print(f"the price is {price:.2f}")
