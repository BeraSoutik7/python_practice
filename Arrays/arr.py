from array import *
vals = array("i",[1,2,3,4])

newArr = array(vals.typecode, (a*a for a in vals))
print(newArr)