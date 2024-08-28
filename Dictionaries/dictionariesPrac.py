dict = {
    "name":"Soutik",
    "age" : 21,
    "Language" : ["Java", "Pthon", "C"],
    "marks" : {
        "java" : 90,
        "python" : 95,
        "c" : 85
    }
}
print(dict)
print(type(dict))
print(dict["age"])
print(dict["name"])
print(dict["Language"])
dict["roll"]=123200902036
print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())

print(dict.get("name"))
dict.update({"city":"Kolkata"})
print(dict)