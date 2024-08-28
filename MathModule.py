# The floor() function:
# floor() method in Python returns the floor of x i.e., the largest integer not greater than x. 

import math as m

a = 1.1
b = 2.68757858 

print(a+b)
print(m.floor(a+b))


# The ceil() Function:
# The method ceil(x) in Python returns a ceiling value of x i.e., the smallest integer greater than or equal to x.

print(m.ceil(a+b))

# Using integer division and addition:
# In this approach, x // 1 is used to obtain the integer part of x, which is equivalent to math.floor(x). To obtain the ceiling of x, we add 1 to the integer part of x.

print((a+b)//1)


# use floor without using floor

print(-int(-(a+b)//1))