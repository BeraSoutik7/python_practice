def sum(a,b):
    return a+b

print(sum("Hello ","World!!"))
print(sum(1,2))


def avg_of_three(a,b,c):
    print(int((a+b+c)/3))

avg_of_three(1,2,2)

def arg_function(b,a,c=10):
    print(a,b,c)
arg_function(99)