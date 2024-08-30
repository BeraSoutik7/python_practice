a = {1,2,3}
print(type(a))
print(a)
a.add("Hello")
print(a)
a.remove("Hello")
print(a)
print(a)

# l = list() Cause list is unhasable
# a.add(l)

# a.clear()
# print(a)

# a.pop()
# print(a)

b = {6,4,5}
print(a.union(b))
print(a.intersection(b))

values = {9,}
print(values)