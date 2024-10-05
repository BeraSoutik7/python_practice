from numpy import *

arr = array([
    [1,2,3,0,0,0],
    [4,5,6,0,0,0],
]
)

print(arr)
print(type(arr))
print(shape(arr))
print(size(arr))

arr1 = arr.flatten()
print(arr1)

arr2 = arr1.reshape(2,2,3)
print(arr2)


m = matrix(arr)
another_m = matrix('1 2 3 4 ; 1 2 3 4')
print(m)
print(another_m)
print(diagonal(another_m))
print(diagonal(m))