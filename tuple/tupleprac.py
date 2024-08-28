# Tuple is immutable

a = (12,15,48,48)
print(type(a))
print(a[0:2])
print(a[-1])
# a[0] = 12 Not Allowed

#Ideal single element tuple

b =(1,)
c = (2)

print(type(a))
print(type(c))

#Index method
print(a.index(15))
print(a.count(48))