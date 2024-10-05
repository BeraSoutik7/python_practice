def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if(a<b):
            return func(b,a)
        else:
            return func(a,b)
    return inner



div = smart_div(div)
div(2,10)