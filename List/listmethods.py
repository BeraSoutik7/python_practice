a = [10,12,17]
b = [8,5]
print(len(a))

# a.append(b)
a.append(2)
print(a)

a.sort(reverse=True)

print(a)
a.insert(-3,0)
print(a)

a.remove(0)
print(a)
a.pop(-1)
print(a)
print(a.count(10))


