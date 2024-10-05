
def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x",x)

a =10
print(id(a))
update(a)
print("a",a)

def update2(lst):
    print(id(lst))
    lst[1]=9999
    print(id(lst))
    print('lst',lst)

lst = [1,2,3]
print(id(lst))
update2(lst)
print(lst)