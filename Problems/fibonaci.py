def fibo(n :int):
    a = 0
    b = 1
    if(n<0):
        print("Not possible...")
        return
    if(n==1):
        print(0)
    else:
        print(0)
        print(1)
    
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)
        
fibo(10)

def fibo_rec(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)
print("Recursive call...")
print(fibo_rec(10))