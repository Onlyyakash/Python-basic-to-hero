dic ={
    "harry": "human being",
    "spoon": "object",
}
print(dic["harry"])
print(dic["spoon"])

dic = {
    111 : "Akash",
    121 : "sana",
    131 : "gulli",
    141 : "badmos",
    }
print(dic[121])


info = {"name": "harry", "age": 20, "student": True}
print(info)
print(info["name"])
print(info["age"])
print(info["is student"])
print(info.get("name"))
print(info.get("age"))
print(info.get("is student"))
print(info.keys())
print(info.values())
print(info.items())
for key in info.keys():
    print(f"the value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"the value corresponding to the key {key} is {value}")
