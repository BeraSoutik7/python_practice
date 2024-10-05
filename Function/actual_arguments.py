#Position
def person(name='user',age=0):
    print(name)
    print(age)

person("soutik",21)

#Keywords
person("soutik",age=21,)
person(age=21,name="Soutik")

#Default
person('soutik')

#variable length
from numpy import *

def add(a,*b):
    arr = array(b)

    print(a+sum(b))
add(1,2,3,4)

#Keyword variable length

def person2(name,**data):
    print(name,data)

person2("Soutik",age=21,Place="Kolkata")

str = "abbo"
lst = set(str)
ans = set(lst)
print(ans)
a=""
for i in ans:
    a+=i

print(a)



