a = 10
def funtest():
    global a
    a = 15
    print(a)
funtest()
print(a)

b = 10
def fun():
    b = 99
    x = globals()['b']
    print(b)
    globals()['b']=2
    print('global',globals()['b'])

fun()