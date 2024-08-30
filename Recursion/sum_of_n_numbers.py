def sumOfNum(n:int)->int:
    if(n==1):
        return 1
    return n + sumOfNum(n-1)

print(sumOfNum(3))